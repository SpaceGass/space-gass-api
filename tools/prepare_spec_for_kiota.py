"""
Prepare the published OpenAPI spec for Kiota client generation.

    python tools/prepare_spec_for_kiota.py [descriptions/openapi.json] [build/openapi.kiota.json]

The published spec (``descriptions/openapi.json``) is written for people
reading the API reference: where a body or response can be one of several
polymorphic types it says so with ``oneOf`` (15 design-code settings, 41
section shapes), which Swagger UI / Zudoku render as a pick-list.

Kiota has no union types, so for every ``oneOf`` it invents a "composed type
wrapper" class with one nullable property per member. That is clumsy to call
(``new X_codeSettings { SteelMemberDesignSettingsAs4100Update = ... }``,
``GetAsSettingsGetResponseAsync()``, 41-property shape wrappers).

Every one of those ``oneOf``s lists subclasses of a single base schema that
carries a discriminator, so the two forms are identical on the wire. This
script writes a copy of the spec for Kiota only, with two changes:

1. **oneOf -> base type.** A ``oneOf`` whose members are all ``$ref``s to
   schemas that share one ``allOf`` base with a discriminator is replaced by a
   ``$ref`` to that base. Kiota then generates plain inheritance:
   ``PatchAsync(SteelMemberDesignSettingsBaseUpdate body)``,
   ``List<SectionShape> Shapes``, and a factory on the base that builds the
   right subclass from the discriminator when reading a response.

2. **Discriminator default.** Each subclass redeclares the discriminator as a
   single-value enum (``"enum": ["Library"]``). That is replaced with a plain
   string ``default``, which Kiota writes into the subclass constructor
   (``ShapeType = "Library"``), so callers never set discriminators by hand.
   (Keeping the enum as well makes Kiota emit C# that does not compile.)

The published spec is never modified. The output path is git-ignored.

Exit code 1 if a ``oneOf`` remains that this script could not convert — it
would become a composed wrapper in the SDK, so decide deliberately whether to
extend the script or accept the wrapper (see ALLOWED_ONEOF).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_IN = REPO / "descriptions" / "openapi.json"
DEFAULT_OUT = REPO / "build" / "openapi.kiota.json"

# JSON-pointer prefixes of oneOf sites that are intentionally left as composed
# wrappers. Empty at build 14.51.12.
ALLOWED_ONEOF: tuple[str, ...] = ()


def _name(ref: str) -> str:
    return ref.rsplit("/", 1)[-1]


def transform(spec: dict) -> tuple[dict, dict]:
    """Returns (transformed spec, report). Mutates and returns ``spec``."""
    schemas = spec["components"]["schemas"]
    report = {"oneof_replaced": [], "oneof_left": [], "discriminator_defaults": 0}

    def common_base(one_of: list) -> str | None:
        if not one_of or not all(isinstance(m, dict) and set(m) == {"$ref"} for m in one_of):
            return None
        bases = set()
        for member in one_of:
            schema = schemas.get(_name(member["$ref"]), {})
            all_of = schema.get("allOf") or []
            refs = [a["$ref"] for a in all_of if isinstance(a, dict) and "$ref" in a]
            if len(refs) != 1:
                return None
            bases.add(refs[0])
        if len(bases) != 1:
            return None
        base = bases.pop()
        return base if "discriminator" in schemas.get(_name(base), {}) else None

    def walk(node, pointer: str) -> None:
        if isinstance(node, dict):
            for key, value in list(node.items()):
                here = f"{pointer}/{key}"
                if isinstance(value, dict) and "oneOf" in value:
                    base = common_base(value["oneOf"])
                    if base:
                        node[key] = {"$ref": base}
                        report["oneof_replaced"].append((here, _name(base), len(value["oneOf"])))
                        continue
                    report["oneof_left"].append(here)
                walk(value, here)
        elif isinstance(node, list):
            for i, value in enumerate(node):
                walk(value, f"{pointer}[{i}]")

    walk(spec, "")

    for schema in schemas.values():
        all_of = schema.get("allOf") or []
        refs = [a["$ref"] for a in all_of if isinstance(a, dict) and "$ref" in a]
        if len(refs) != 1:
            continue
        discriminator = schemas.get(_name(refs[0]), {}).get("discriminator", {}).get("propertyName")
        prop = (schema.get("properties") or {}).get(discriminator) if discriminator else None
        if prop and len(prop.get("enum") or []) == 1:
            prop["default"] = prop.pop("enum")[0]
            report["discriminator_defaults"] += 1

    return spec, report


def main(argv: list[str]) -> int:
    src = Path(argv[1]) if len(argv) > 1 else DEFAULT_IN
    dst = Path(argv[2]) if len(argv) > 2 else DEFAULT_OUT

    spec, report = transform(json.loads(src.read_text(encoding="utf-8")))

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(spec, indent=2), encoding="utf-8")

    by_base: dict[str, int] = {}
    for _, base, _ in report["oneof_replaced"]:
        by_base[base] = by_base.get(base, 0) + 1
    print(f"wrote {dst}")
    print(f"  oneOf -> base type: {len(report['oneof_replaced'])} site(s) "
          + ", ".join(f"{b} x{n}" for b, n in sorted(by_base.items())))
    print(f"  discriminator defaults: {report['discriminator_defaults']} subclass(es)")

    unexpected = [p for p in report["oneof_left"] if not p.startswith(ALLOWED_ONEOF or ("\0",))]
    if unexpected:
        print("ERROR: oneOf left unconverted (would become a Kiota composed wrapper):")
        for pointer in unexpected:
            print("  -", pointer)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
