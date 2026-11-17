"""
Post-regen check that the SDKs are free of Kiota composed-type wrappers and
that the hand-maintained steel design helpers still fit.

Run from the repo root after ``tools/regen_python_inits.py``::

    python tools/check_helpers.py

What it verifies:

1. ``tools/prepare_spec_for_kiota.py`` converts every ``oneOf`` in the
   published spec (none left behind -> none becomes a wrapper class).
2. Neither generated tree contains a composed-type wrapper — i.e. the clients
   really were generated from the transformed spec, not the published one.
3. Every subclass of a discriminated base sets its discriminator in the
   constructor / as a field default, so callers never set ``shapeType`` or
   ``code`` by hand.
4. The polymorphic properties have the base types the examples and helpers
   rely on (``Shapes: List<SectionShape>``, ``CodeSettings``, ``Settings``
   GET/PATCH), and the Python ``steel_member`` helpers import.

Exit code 1 and a list of problems on failure. C# type renames are caught by
``dotnet build sdks/csharp/client/SpaceGassApi/SpaceGassApi.csproj``.
"""

from __future__ import annotations

import copy
import dataclasses
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SPEC = REPO / "descriptions" / "openapi.json"
CS_GEN = REPO / "sdks" / "csharp" / "client" / "SpaceGassApi" / "Generated"
CS_MODELS = CS_GEN / "Models"
PY_PKG = REPO / "sdks" / "python" / "client" / "space_gass_api"
PY_GEN = PY_PKG / "generated"

sys.path.insert(0, str(PY_PKG.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

problems: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        problems.append(msg)


def main() -> int:
    from prepare_spec_for_kiota import ALLOWED_ONEOF, transform

    published = json.loads(SPEC.read_text(encoding="utf-8"))
    spec, report = transform(copy.deepcopy(published))
    schemas = spec["components"]["schemas"]

    # ---- 1. every oneOf is converted ---------------------------------------
    left = [p for p in report["oneof_left"] if not p.startswith(ALLOWED_ONEOF or ("\0",))]
    check(not left, f"oneOf not converted by prepare_spec_for_kiota.py (will become a wrapper): {left}")

    # ---- 2. no composed wrappers in the generated clients --------------------
    cs_wrappers = [str(p.relative_to(CS_GEN)) for p in CS_GEN.rglob("*.cs")
                   if "IComposedTypeWrapper" in p.read_text(encoding="utf-8")]
    py_wrappers = [str(p.relative_to(PY_GEN)) for p in PY_GEN.rglob("*.py")
                   if "ComposedTypeWrapper" in p.read_text(encoding="utf-8")]
    hint = " — regenerate from build/openapi.kiota.json (tools/prepare_spec_for_kiota.py), not the published spec"
    check(not cs_wrappers, f"C# composed wrappers present: {cs_wrappers[:5]}{hint}")
    check(not py_wrappers, f"Python composed wrappers present: {py_wrappers[:5]}{hint}")

    # ---- 3. discriminators are defaulted in every subclass -------------------
    import space_gass_api.models as models  # noqa: E402

    subclasses: dict[str, tuple[str, str]] = {}   # class -> (discriminator property, value)
    for name, schema in schemas.items():
        refs = [a["$ref"] for a in (schema.get("allOf") or []) if isinstance(a, dict) and "$ref" in a]
        if len(refs) != 1:
            continue
        base = schemas[refs[0].rsplit("/", 1)[-1]]
        prop = base.get("discriminator", {}).get("propertyName")
        value = (schema.get("properties") or {}).get(prop, {}).get("default") if prop else None
        if value is not None:
            subclasses[name] = (prop, value)

    check(report["discriminator_defaults"] == len(subclasses) and subclasses,
          "prepare_spec_for_kiota.py did not default every subclass discriminator")

    for name, (prop, value) in subclasses.items():
        cs_file = CS_MODELS / f"{name}.cs"
        if not cs_file.exists():
            check(False, f"C# model {name}.cs missing")
            continue
        cs_prop = prop[:1].upper() + prop[1:]
        check(f'{cs_prop} = "{value}";' in cs_file.read_text(encoding="utf-8"),
              f"C# {name} does not default {cs_prop} to \"{value}\" in its constructor")

        cls = getattr(models, name, None)
        if cls is None:
            check(False, f"Python models has no {name}")
            continue
        py_attr = re.sub(r"(?<!^)(?=[A-Z])", "_", prop).lower()
        check(getattr(cls(), py_attr, None) == value,
              f"Python {name}().{py_attr} is not \"{value}\"")

    # ---- 4. polymorphic properties are base-typed; helpers import ------------
    def cs_has(path: Path, needle: str, what: str) -> None:
        check(needle in path.read_text(encoding="utf-8"), f"C# {what}: expected `{needle}` in {path.name}")

    cs_has(CS_MODELS / "SectionShapeBuilderCreate.cs", "List<global::SpaceGassApi.Models.SectionShape>? Shapes", "shape list type")
    cs_has(CS_MODELS / "Section.cs", "List<global::SpaceGassApi.Models.SectionShape>? Shapes", "shape list type")
    for request in ("SteelMemberDesignRunCheckRequest", "SteelMemberDesignRunDesignRequest"):
        cs_has(CS_MODELS / f"{request}.cs", "SteelMemberDesignSettingsBaseUpdate? CodeSettings", "code settings type")
    settings_builder = CS_GEN / "Job" / "Design" / "SteelMember" / "Item" / "Settings" / "SettingsRequestBuilder.cs"
    cs_has(settings_builder, "Task<global::SpaceGassApi.Models.SteelMemberDesignSettingsBase?> GetAsync(", "settings GET")
    cs_has(settings_builder, "PatchAsync(global::SpaceGassApi.Models.SteelMemberDesignSettingsBaseUpdate body", "settings PATCH")

    def py_field(cls, field: str) -> str:
        return next((str(f.type) for f in dataclasses.fields(cls) if f.name == field), "<missing>")

    check(py_field(models.SectionShapeBuilderCreate, "shapes") == "Optional[list[SectionShape]]",
          f"Python SectionShapeBuilderCreate.shapes is {py_field(models.SectionShapeBuilderCreate, 'shapes')}")
    check(py_field(models.SteelMemberDesignRunCheckRequest, "code_settings") == "Optional[SteelMemberDesignSettingsBaseUpdate]",
          f"Python SteelMemberDesignRunCheckRequest.code_settings is {py_field(models.SteelMemberDesignRunCheckRequest, 'code_settings')}")

    from space_gass_api import steel_member  # noqa: E402

    for fn in ("get_settings", "patch_settings"):
        check(callable(getattr(steel_member, fn, None)), f"steel_member.{fn} missing")
    codes = set(schemas["SteelMemberDesignSettingsBase"]["discriminator"]["mapping"])
    check({e.value for e in models.DesignCode} <= codes,
          f"DesignCode enum has values with no settings class: {sorted({e.value for e in models.DesignCode} - codes)}")

    # ---- 5. DesignCode.ToString() is the route segment ----------------------
    # Examples select a design code with `SteelMember[DesignCode.X.ToString()]`.
    # That only works while Kiota keeps each C# member name equal to its wire
    # value; a value Kiota has to sanitise (a dash, a leading digit) would break it.
    design_code_cs = (CS_MODELS / "DesignCode.cs").read_text(encoding="utf-8")
    cs_pairs = re.findall(
        r'EnumMember\(Value = "([^"]+)"\)\]\s*(?:#pragma[^\n]*\n\s*)?(\w+),', design_code_cs)
    renamed = [(value, name) for value, name in cs_pairs if value != name]
    check(not renamed, f"C# DesignCode member names differ from wire values {renamed}: "
                       "`SteelMember[code.ToString()]` would send the wrong route segment")
    check({value for value, _ in cs_pairs} == set(published["components"]["schemas"]["DesignCode"]["enum"]),
          "C# DesignCode enum does not match the spec's DesignCode values")

    if problems:
        print("SDK shape check FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    by_base: dict[str, int] = {}
    for prop, _ in subclasses.values():
        by_base[prop] = by_base.get(prop, 0) + 1
    print("SDK shape check passed: no composed wrappers; %d oneOf site(s) generated as base types; "
          "discriminator defaults on %d subclasses (%s)."
          % (len(report["oneof_replaced"]), len(subclasses),
             ", ".join(f"{n} by {p}" for p, n in sorted(by_base.items()))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
