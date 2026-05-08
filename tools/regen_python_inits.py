"""
Post-Kiota regenerator for the Python SDK's `__init__.py` aggregators.

Kiota generates `sdks/python/client/space_gass_api/` as a PEP 420
namespace package — no `__init__.py` files anywhere in the tree. That
makes `import space_gass_api.models as models` + `models.NodeCreate`
fail to resolve, and prevents us from attaching `create_client` as a
static method on `SpaceGassApiClient`.

This script writes two `__init__.py` files inside the generated tree:

  1. `space_gass_api/__init__.py`
       - imports SpaceGassApiClient
       - imports create_client from the hand-maintained
         `space_gass_api_extensions` top-level module
       - attaches it as a static method on the client class
       - re-exports SpaceGassApiClient

  2. `space_gass_api/models/__init__.py`
       - re-exports every model class from the snake_case submodules
         so callers can write `models.NodeCreate` etc.

Idempotent — rerunning produces byte-identical output.

Run this whenever Kiota regenerates the SDK. CI does it automatically
in `.github/workflows/generate-clients.yml`. For local regens:

    python tools/regen_python_inits.py
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PY_CLIENT = REPO_ROOT / "sdks" / "python" / "client"
PKG_DIR = PY_CLIENT / "space_gass_api"
MODELS_DIR = PKG_DIR / "models"

PKG_INIT = PKG_DIR / "__init__.py"
MODELS_INIT = MODELS_DIR / "__init__.py"

CLASS_RE = re.compile(r"^class\s+([A-Z][A-Za-z0-9_]*)\b", re.MULTILINE)

PKG_INIT_CONTENTS = '''"""
Auto-generated post-Kiota by `tools/regen_python_inits.py` — DO NOT EDIT.

Imports the generated `SpaceGassApiClient`, attaches the
`create_client` factory and re-exports the `query` helper from the
hand-maintained `space_gass_api_extensions` module.

Usage:

    from space_gass_api import SpaceGassApiClient, query
    import space_gass_api.models as models

    client = SpaceGassApiClient.create_client()
    node = await client.job.structure.nodes.post(models.NodeCreate(x=0, y=0, z=0))
    restrained = await query(client.job.structure.nodes,
                             node_type=models.NodeTypeFilter.Restrained)
"""

from .space_gass_api_client import SpaceGassApiClient
from space_gass_api_extensions import create_client, query

SpaceGassApiClient.create_client = staticmethod(create_client)

__all__ = ["SpaceGassApiClient", "query"]
'''


def collect_model_classes() -> list[tuple[str, str]]:
    """Return [(module_stem, ClassName), ...] sorted by (module, class)."""
    out: list[tuple[str, str]] = []
    for path in sorted(MODELS_DIR.glob("*.py")):
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
    lines.append("Aggregator that re-exports every model class so callers can write:")
    lines.append("")
    lines.append("    import space_gass_api.models as models")
    lines.append("    body = models.NodeCreate(x=0, y=0, z=0)")
    lines.append('"""')
    lines.append("")
    for module, cls in entries:
        lines.append(f"from .{module} import {cls}")
    lines.append("")
    lines.append("__all__ = [")
    for _, cls in entries:
        lines.append(f'    "{cls}",')
    lines.append("]")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    if not MODELS_DIR.is_dir():
        raise SystemExit(
            f"models dir not found: {MODELS_DIR}\n"
            "Has the Python SDK been generated yet? Run the kiota generate "
            "step first, then rerun this script."
        )

    entries = collect_model_classes()
    if not entries:
        raise SystemExit(f"no model classes found under {MODELS_DIR}")

    PKG_INIT.write_text(PKG_INIT_CONTENTS, encoding="utf-8")
    MODELS_INIT.write_text(render_models_init(entries), encoding="utf-8")

    print(f"wrote {PKG_INIT.relative_to(REPO_ROOT)}")
    print(f"wrote {MODELS_INIT.relative_to(REPO_ROOT)} ({len(entries)} model re-exports)")


if __name__ == "__main__":
    main()
