"""
Post-Kiota regenerator for the Python SDK's ``__init__.py`` aggregators.

Kiota generates into ``space_gass_api/generated/`` as a PEP 420
namespace package — no ``__init__.py`` files anywhere in the tree. That
makes ``import space_gass_api.models as models`` + ``models.NodeCreate``
fail to resolve.

This script does four things after Kiota regeneration:

  1. Writes ``space_gass_api/__init__.py``
       - calls ``_enhance_get_methods()`` to enable ``.get(**kwargs)``
       - imports and re-exports ``SpaceGassApiClient``

  2. Writes ``space_gass_api/__init__.pyi``
       - type stub so Pyright / Pylance resolves ``SpaceGassApiClient``

  3. Writes ``space_gass_api/models/__init__.py``
       - re-exports every model class from the generated submodules
         so callers can write ``models.NodeCreate`` etc.

  4. Injects ``@overload`` stubs into every ``*_request_builder.py``
       whose class body contains a ``GetQueryParameters`` dataclass,
       so Pyright / Pylance shows the keyword arguments in IntelliSense
       when users call ``.get(node_type=..., limit=...)``.

Idempotent — rerunning produces byte-identical output.

Run this whenever Kiota regenerates the SDK. CI does it automatically
in ``.github/workflows/generate-clients.yml``. For local regens::

    python tools/regen_python_inits.py
"""

from __future__ import annotations

import ast
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PY_CLIENT = REPO_ROOT / "sdks" / "python" / "client"
PKG_DIR = PY_CLIENT / "space_gass_api"
GENERATED_DIR = PKG_DIR / "generated"
MODELS_SRC = GENERATED_DIR / "models"
MODELS_SHIM = PKG_DIR / "models"

PKG_INIT = PKG_DIR / "__init__.py"
PKG_INIT_PYI = PKG_DIR / "__init__.pyi"
MODELS_INIT = MODELS_SHIM / "__init__.py"

CLASS_RE = re.compile(r"^class\s+([A-Z][A-Za-z0-9_]*)\b", re.MULTILINE)

PKG_INIT_CONTENTS = '''"""
Auto-generated post-Kiota by `tools/regen_python_inits.py` — DO NOT EDIT.

Wires up the hand-maintained extensions on top of the Kiota-generated
client:

- ``SpaceGassApiClient`` extends the generated ``BaseApiClient``
  with the ``create_client()`` factory method.

- ``.get(**kwargs)`` is auto-enhanced on every builder that has GET
  query parameters, so callers can pass filters as keyword arguments
  directly instead of constructing ``RequestConfiguration`` objects.

Usage:

    from space_gass_api import SpaceGassApiClient
    import space_gass_api.models as models

    client = SpaceGassApiClient.create_client()
    node = await client.job.structure.nodes.post(models.NodeCreate(x=0, y=0, z=0))
    restrained = await client.job.structure.nodes.get(
        node_type=models.NodeTypeFilter.Restrained)
"""

from .space_gass_api_client import _enhance_get_methods

_enhance_get_methods()

from .space_gass_api_client import SpaceGassApiClient

__all__ = ["SpaceGassApiClient"]
'''

PKG_INIT_STUB = '''# Auto-generated post-Kiota by `tools/regen_python_inits.py` — DO NOT EDIT.
from .space_gass_api_client import SpaceGassApiClient as SpaceGassApiClient

__all__: list[str]
'''


def collect_model_classes() -> list[tuple[str, str]]:
    """Return [(module_stem, ClassName), ...] sorted by (module, class)."""
    out: list[tuple[str, str]] = []
    for path in sorted(MODELS_SRC.glob("*.py")):
        if path.name.startswith("__"):
            continue
        text = path.read_text(encoding="utf-8")
        for cls in CLASS_RE.findall(text):
            out.append((path.stem, cls))
    return out


def render_models_init(entries: list[tuple[str, str]]) -> str:
    lines: list[str] = []
    lines.append('"""')
    lines.append("Auto-generated post-Kiota by `tools/regen_python_inits.py` — DO NOT EDIT.")
    lines.append("")
    lines.append("Re-exports every model class from the generated submodules so callers")
    lines.append("can write:")
    lines.append("")
    lines.append("    import space_gass_api.models as models")
    lines.append("    body = models.NodeCreate(x=0, y=0, z=0)")
    lines.append('"""')
    lines.append("")
    for module, cls in entries:
        lines.append(f"from ..generated.models.{module} import {cls}")
    lines.append("")
    lines.append("__all__ = [")
    for _, cls in entries:
        lines.append(f'    "{cls}",')
    lines.append("]")
    lines.append("")
    return "\n".join(lines)


OVERLOAD_BANNER = "    # --- @overload added by regen_python_inits.py ---"
OVERLOAD_FENCE = "    # --- end overloads ---"


def _parse_builder(source: str) -> tuple[str, list[tuple[str, str]], str] | None:
    """Extract overload info from a builder module.

    Returns ``(qp_class_name, [(field, type_str), ...], return_type_str)``
    or ``None`` if the builder has no ``GetQueryParameters``.
    """
    tree = ast.parse(source)

    builder = next(
        (n for n in ast.iter_child_nodes(tree)
         if isinstance(n, ast.ClassDef) and n.name.endswith("RequestBuilder")),
        None,
    )
    if builder is None:
        return None

    qp_name = f"{builder.name}GetQueryParameters"
    qp_cls = next(
        (n for n in ast.iter_child_nodes(builder)
         if isinstance(n, ast.ClassDef) and n.name == qp_name),
        None,
    )
    if qp_cls is None:
        return None

    fields = [
        (n.target.id, ast.unparse(n.annotation))
        for n in ast.iter_child_nodes(qp_cls)
        if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name)
    ]
    if not fields:
        return None

    get_m = next(
        (n for n in ast.iter_child_nodes(builder)
         if isinstance(n, (ast.AsyncFunctionDef, ast.FunctionDef))
         and n.name == "get"),
        None,
    )
    if get_m is None or get_m.returns is None:
        return None

    return qp_name, fields, ast.unparse(get_m.returns)


def _strip_overloads(source: str) -> str:
    """Remove previously injected overload blocks for idempotency."""
    while OVERLOAD_BANNER in source:
        start = source.index(OVERLOAD_BANNER)
        try:
            end = source.index(OVERLOAD_FENCE, start) + len(OVERLOAD_FENCE)
        except ValueError:
            break
        if end < len(source) and source[end] == "\n":
            end += 1
        source = source[:start] + source[end:]
    return source.replace(", **kwargs) ->", ") ->")


def _inject_overloads(
    source: str,
    qp_name: str,
    fields: list[tuple[str, str]],
    ret_type: str,
) -> str:
    """Inject ``@overload`` stubs and ``**kwargs`` into a builder source."""
    lines = source.splitlines(keepends=True)

    # Ensure 'overload' is in the typing imports
    for i, line in enumerate(lines):
        if line.startswith("from typing import") and "overload" not in line:
            lines[i] = line.rstrip("\n").rstrip() + ", overload\n"
            break

    # Find the `async def get(self,` line
    get_idx = next(
        (i for i, ln in enumerate(lines)
         if ln.strip().startswith("async def get(self")),
        None,
    )
    if get_idx is None:
        return source

    # Add **kwargs to the implementation signature
    lines[get_idx] = lines[get_idx].replace(") ->", ", **kwargs) ->")

    # Build the overload block
    ind = "    "
    block: list[str] = []
    block.append(f"{OVERLOAD_BANNER}\n")
    block.append(f"{ind}@overload\n")
    block.append(f"{ind}async def get(\n")
    block.append(f"{ind}    self,\n")
    block.append(f"{ind}    *,\n")
    for fname, ftype in fields:
        block.append(f"{ind}    {fname}: {ftype} = None,\n")
    block.append(f"{ind}) -> {ret_type}: ...\n")
    block.append(f"{ind}@overload\n")
    rc = f"Optional[RequestConfiguration[{qp_name}]]"
    block.append(
        f"{ind}async def get(self, request_configuration: "
        f"{rc} = None) -> {ret_type}: ...\n"
    )
    block.append(f"{OVERLOAD_FENCE}\n")

    # Insert block right before the get method
    for j, bl in enumerate(block):
        lines.insert(get_idx + j, bl)

    return "".join(lines)


def enhance_builder_get_methods() -> int:
    """Inject ``@overload`` stubs into every builder with GetQueryParameters.

    This gives Pyright / Pylance the typed kwargs signature so
    IntelliSense shows the available query parameters.

    Idempotent — strips previous injections before re-applying.
    """
    count = 0
    for path in sorted(GENERATED_DIR.rglob("*_request_builder.py")):
        source = path.read_text(encoding="utf-8")
        clean = _strip_overloads(source)

        info = _parse_builder(clean)
        if info is None:
            if clean != source:
                path.write_text(clean, encoding="utf-8")
            continue

        qp_name, fields, ret_type = info
        modified = _inject_overloads(clean, qp_name, fields, ret_type)

        if modified != source:
            path.write_text(modified, encoding="utf-8")
            count += 1

    return count


def main() -> None:
    if not MODELS_SRC.is_dir():
        raise SystemExit(
            f"generated models dir not found: {MODELS_SRC}\n"
            "Has the Python SDK been generated yet? Run the kiota generate "
            "step first, then rerun this script."
        )

    entries = collect_model_classes()
    if not entries:
        raise SystemExit(f"no model classes found under {MODELS_SRC}")

    # Create the models shim directory (outside generated/, safe from
    # --clean-output). This re-exports generated models so users can
    # write `import space_gass_api.models as models`.
    MODELS_SHIM.mkdir(exist_ok=True)

    PKG_INIT.write_text(PKG_INIT_CONTENTS, encoding="utf-8")
    PKG_INIT_PYI.write_text(PKG_INIT_STUB, encoding="utf-8")
    MODELS_INIT.write_text(render_models_init(entries), encoding="utf-8")

    enhanced = enhance_builder_get_methods()

    print(f"wrote {PKG_INIT.relative_to(REPO_ROOT)}")
    print(f"wrote {PKG_INIT_PYI.relative_to(REPO_ROOT)}")
    print(f"wrote {MODELS_INIT.relative_to(REPO_ROOT)} ({len(entries)} model re-exports)")
    print(f"enhanced {enhanced} builder(s) with @overload stubs")


if __name__ == "__main__":
    main()
