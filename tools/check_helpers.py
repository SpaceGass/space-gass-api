"""
Post-regen check for the hand-maintained oneOf helpers.

The helpers under ``sdks/csharp/client/SpaceGassApi/Utils/`` and at the
``space_gass_api`` package root carry knowledge that Kiota does not emit:
the class -> discriminator map for ``SectionShape``, and the class-name
convention the generic design-code settings helpers resolve wrappers by. A regen can silently change the spec mapping, add shape types, or
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
        names = {t for t, p in props if t in spec_map}
        check(names == set(spec_map),
              f"C# {wrapper}_shapes wrapper has no property typed as some shape classes: "
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

    # ---- Design-code settings (generic helpers) ---------------------------
    # The steel member design helpers are generic: they find the wrapper
    # property/field by the settings class name. Check that convention still
    # holds for every design code in the spec, in both SDKs.
    codes = sorted(schemas["SteelMemberDesignSettingsBaseUpdate"]["discriminator"]["mapping"])
    check(codes == sorted(schemas["SteelMemberDesignSettingsBase"]["discriminator"]["mapping"]),
          "Design codes differ between SteelMemberDesignSettingsBase and ...BaseUpdate")

    cs_steel = (CS_UTILS / "SteelMemberDesignExtensions.cs").read_text(encoding="utf-8")
    for needed in ("SteelMemberDesignRunCheckRequest_codeSettings", "SteelMemberDesignRunDesignRequest_codeSettings",
                   "SettingsPatchRequestBody", "GetAsSettingsGetResponseAsync", "PatchAsSettingsPatchResponseAsync"):
        check(needed in cs_steel, f"SteelMemberDesignExtensions.cs no longer references {needed}")

    cs_wrappers = {
        "SteelMemberDesignRunCheckRequest": (CS_MODELS / "SteelMemberDesignRunCheckRequest.cs", "Update"),
        "SteelMemberDesignRunDesignRequest": (CS_MODELS / "SteelMemberDesignRunDesignRequest.cs", "Update"),
        "SettingsRequestBuilder (patch body)": (
            CS_MODELS.parent / "Job" / "Design" / "SteelMember" / "Item" / "Settings" / "SettingsRequestBuilder.cs", "Update"),
        "SettingsRequestBuilder (responses)": (
            CS_MODELS.parent / "Job" / "Design" / "SteelMember" / "Item" / "Settings" / "SettingsRequestBuilder.cs", ""),
    }
    for label, (path, suffix) in cs_wrappers.items():
        text = path.read_text(encoding="utf-8")
        missing = [c for c in codes
                   if not re.search(rf"\.SteelMemberDesignSettings{c}{suffix}\? \w+ \{{ get; set; \}}", text)]
        check(not missing, f"C# {label}: no wrapper property typed as the settings class for {missing}")

    import space_gass_api.models as models  # noqa: E402
    from space_gass_api import steel_member  # noqa: E402
    from space_gass_api.generated.job.design.steel_member.item.settings.settings_get_response import (  # noqa: E402
        SettingsGetResponse,
    )
    from space_gass_api.generated.job.design.steel_member.item.settings.settings_patch_request_body import (  # noqa: E402
        SettingsPatchRequestBody,
    )

    for c in codes:
        update_cls = getattr(models, f"SteelMemberDesignSettings{c}Update", None)
        settings_cls = getattr(models, f"SteelMemberDesignSettings{c}", None)
        if update_cls is None or settings_cls is None:
            check(False, f"Python models have no SteelMemberDesignSettings{c}[Update] class")
            continue
        try:
            steel_member.run_check_request(code_settings=update_cls())
            steel_member.run_design_request(code_settings=update_cls())
            body = steel_member.code_settings_body(update_cls())
            check(isinstance(body, SettingsPatchRequestBody), f"code_settings_body failed for {c}")
        except TypeError as ex:
            check(False, f"steel_member helpers cannot wrap {c}: {ex}")
        check(steel_member._wrapper_field(SettingsGetResponse, settings_cls) is not None,
              f"Python SettingsGetResponse has no field for SteelMemberDesignSettings{c}")

    design_code_enum = {e.value for e in models.DesignCode}
    check(design_code_enum <= set(codes),
          f"DesignCode enum has values with no settings class: {sorted(design_code_enum - set(codes))}")

    # ---- Smoke: the shape helpers still round-trip ---------------------------
    wrapped = shape_builder.shapes(models.LibraryShape(library="x", name="y"), models.RectangularBarShape(d=1, b=2))
    back = shape_builder.shapes_of(models.SectionShapeBuilderCreate(name="t", shapes=wrapped))
    check([s.shape_type for s in back] == ["Library", "RectangularBar"], "shape_builder round-trip failed")

    if problems:
        print("Helper check FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print("Helper check passed: shape map (%d types), wrapper fields, %d design codes."
          % (len(spec_map), len(codes)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
