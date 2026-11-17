# steel_design_optimise

Builds the simply-supported beam from `create_simple_beam` on a deliberately heavy 610 UB 125, analyses it, looks up the default section library's groups and the scan code of the group the beam's section belongs to, then runs a steel member **DESIGN** to AS 4100 that selects the lightest adequate section from that group, swaps it into the model, re-runs the static analysis and iterates until the design settles. Prints what the run did (iterations, sections updated, analysis re-run), the section it chose, and the check summary for the final section.

See `steel_design_check` for a CHECK run that leaves the model unchanged.

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
