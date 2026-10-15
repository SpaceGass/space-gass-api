# built_up_section

Creates a built-up (shape-builder) section — a 360 UB 44.7 with a 250 x 16 cover plate welded to its top flange — and applies it to a simply-supported beam. Shows the preview endpoint (geometry and numbered reference points without writing anything), anchoring one shape onto another, the computed section properties against the plain UB, and reading the shapes back.

Uses the `shape_builder` helpers (`from space_gass_api import shape_builder`) so plain shape objects can be passed in the `shapes` list and read back typed, without Kiota's per-shape oneOf wrapper.

## Run it

1. Start the SPACE GASS API service.
2. Install dependencies:
   ```
   pip install space-gass-api
   ```
3. From this folder:
   ```
   python built_up_section.py
   ```

The example saves the model to `~/Desktop/SpaceGass Examples-py/BuiltUpSection.sg` so you can open it in SPACE GASS Desktop and view the section.
