"""
Post-regen check for the hand-maintained oneOf helpers.

The helpers under ``sdks/csharp/client/SpaceGassApi/Utils/`` and at the
``space_gass_api`` package root carry knowledge that Kiota does not emit:
the class -> discriminator maps for ``SectionShape`` and the design-code
settings. A regen can silently change the spec mapping, add shape types, or
rename the composed wrapper properties these helpers rely on. This script
compares them.

Run from the repo root after ``tools/regen_python_inits.py``::

    python tools/check_helpers.py

Exit code 1 and a list of mismatches on failure. The C# side is covered by
``dotnet build sdks/csharp/client/SpaceGassApi/SpaceGassApi.csproj`` for type
renames; this script covers the data (maps and property names) in both SDKs.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SPEC = REPO / "descriptions" / "openapi.json"
CS_UTILS = REPO / "sdks" / "csharp" / "client" / "SpaceGassApi" / "Utils"
CS_MODELS = REPO / "sdks" / "csharp" / "client" / "SpaceGassApi" / "Generated" / "Models"
PY_PKG = REPO / "sdks" / "python" / "client" / "space_gass_api"

sys.path.insert(0, str(PY_PKG.parent))

problems: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        problems.append(msg)


def main() -> int:
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    schemas = spec["components"]["schemas"]

    # ---- SectionShape discriminator map ---------------------------------
    spec_map = {
        ref.rsplit("/", 1)[-1]: key
        for key, ref in schemas["SectionShape"]["discriminator"]["mapping"].items()
    }

    cs_text = (CS_UTILS / "SectionShapeExtensions.cs").read_text(encoding="utf-8")
    cs_map = dict(re.findall(r'\[typeof\((\w+)\)\]\s*=\s*"(\w+)"', cs_text))
    check(cs_map == spec_map,
          f"SectionShapeExtensions.cs discriminator map differs from spec: "
          f"missing={sorted(set(spec_map) - set(cs_map))} extra={sorted(set(cs_map) - set(spec_map))} "
          f"changed={sorted(k for k in spec_map.keys() & cs_map.keys() if spec_map[k] != cs_map[k])}")

    from space_gass_api import shape_builder  # noqa: E402

    check(shape_builder.DISCRIMINATORS == spec_map,
          f"shape_builder.DISCRIMINATORS differs from spec: "
          f"missing={sorted(set(spec_map) - set(shape_builder.DISCRIMINATORS))} "
          f"extra={sorted(set(shape_builder.DISCRIMINATORS) - set(spec_map))}")

    # ---- Composed wrapper property names (C#: class name; Python: dataclass field type)
    for wrapper in ("SectionShapeBuilderCreate", "Section"):
        text = (CS_MODELS / f"{wrapper}.cs").read_text(encoding="utf-8")
        props = set(re.findall(r"public global::SpaceGassApi\.Models\.(\w+)\? (\w+) \{ get; set; \}", text))
        names = {p for t, p in props if t == p and t in spec_map}
        check(names == set(spec_map),
              f"C# {wrapper}_shapes wrapper properties no longer match class names: "
              f"missing={sorted(set(spec_map) - names)}")

    from space_gass_api.generated.models.section_shape_builder_create_shapes import (  # noqa: E402
        SectionShapeBuilderCreate_shapes,
    )
    from space_gass_api.generated.models.section_shapes import Section_shapes  # noqa: E402

    for cls in (SectionShapeBuilderCreate_shapes, Section_shapes):
        fields = shape_builder._wrapper_fields(cls)
        check(set(fields) == set(spec_map),
              f"Python {cls.__name__} fields no longer match shape classes: "
              f"missing={sorted(set(spec_map) - set(fields))}")

    # ---- Design-code settings discriminator ------------------------------
    code_map = schemas["SteelMemberDesignSettingsBase"]["discriminator"]["mapping"]
    from space_gass_api import steel_design  # noqa: E402

    check(set(code_map) == {steel_design.AS4100, steel_design.NZS3404},
          f"Design codes in spec {sorted(code_map)} differ from steel_design constants — "
          "add helpers for the new code in steel_design.py and SteelDesignExtensions.cs")

    cs_steel = (CS_UTILS / "SteelDesignExtensions.cs").read_text(encoding="utf-8")
    for code in code_map:
        check(f'"{code}"' in cs_steel, f"SteelDesignExtensions.cs has no constant for design code {code}")

    # Wrapper classes the steel helpers rely on still exist with the expected properties.
    for wrapper, prop in (
        ("SteelDesignRunCheckRequest", "SteelMemberDesignSettingsAS4100Update"),
        ("SteelDesignRunDesignRequest", "SteelMemberDesignSettingsAS4100Update"),
    ):
        text = (CS_MODELS / f"{wrapper}.cs").read_text(encoding="utf-8")
        check(f"{prop}? {prop} {{ get; set; }}" in text,
              f"C# {wrapper}_codeSettings wrapper no longer has {prop}")

    from space_gass_api.generated.models.steel_design_run_check_request_code_settings import (  # noqa: E402
        SteelDesignRunCheckRequest_codeSettings,
    )
    import dataclasses  # noqa: E402

    names = {f.name for f in dataclasses.fields(SteelDesignRunCheckRequest_codeSettings)}
    check({"steel_member_design_settings_a_s4100_update", "steel_member_design_settings_n_z_s3404_update"} <= names,
          f"Python SteelDesignRunCheckRequest_codeSettings fields changed: {sorted(names)}")

    # ---- Smoke: the helpers still round-trip --------------------------------
    import space_gass_api.models as models  # noqa: E402

    wrapped = shape_builder.shapes(models.LibraryShape(library="x", name="y"), models.RectangularBarShape(d=1, b=2))
    back = shape_builder.shapes_of(models.SectionShapeBuilderCreate(name="t", shapes=wrapped))
    check([s.shape_type for s in back] == ["Library", "RectangularBar"], "shape_builder round-trip failed")

    req = steel_design.run_check_request(code_settings=models.SteelMemberDesignSettingsAS4100Update())
    check(req.code_settings.steel_member_design_settings_a_s4100_update.code == steel_design.AS4100,
          "steel_design.run_check_request did not fill the code discriminator")

    if problems:
        print("Helper check FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print("Helper check passed: shape map (%d types), wrapper fields, design codes %s."
          % (len(spec_map), sorted(code_map)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
