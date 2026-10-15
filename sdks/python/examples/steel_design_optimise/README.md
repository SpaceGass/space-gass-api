# steel_design_optimise

Builds the simply-supported beam from `create_simple_beam` on a deliberately heavy 610 UB 125, analyses it, then runs a steel member **DESIGN** to AS 4100 that selects the lightest adequate section from the default section library, swaps it into the model, re-runs the static analysis and iterates until the design settles. Prints what the run did (iterations, sections updated, analysis re-run), the section it chose, and the check summary for the final section.

See `steel_design_check` for a CHECK run that leaves the model unchanged.

Uses the `steel_design` helpers (`from space_gass_api import steel_design`) to build the run request.

## Run it

1. Start the SPACE GASS API service (a licence for the AS 4100 steel member design module is required).
2. Install dependencies:
   ```
   pip install space-gass-api
   ```
3. From this folder:
   ```
   python steel_design_optimise.py
   ```

The example saves the model to `~/Desktop/SpaceGass Examples-py/SteelDesignOptimise.sg` so you can open it in SPACE GASS Desktop and see the selected section.
