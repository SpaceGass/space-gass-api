# steel_design_check

Builds the simply-supported beam from `create_simple_beam`, analyses it, then runs a steel member design **CHECK** to AS 4100: lists the design codes this seat is licensed for, creates a steel member design group, sets the general and AS 4100 settings, starts the check run, polls it to completion and prints the per-member check summary (load factor, critical case, failure mode).

A check verifies the members' current sections without changing the model. See `steel_design_optimise` for a DESIGN run that selects new sections.

Uses the `steel_design` helpers (`from space_gass_api import steel_design`) so the AS 4100 settings object can be passed straight to the run request without Kiota's oneOf wrapper.

## Run it

1. Start the SPACE GASS API service (a licence for the AS 4100 steel member design module is required).
2. Install dependencies:
   ```
   pip install space-gass-api
   ```
3. From this folder:
   ```
   python steel_design_check.py
   ```

The example saves the model to `~/Desktop/SpaceGass Examples-py/SteelDesignCheck.sg` so you can open it in SPACE GASS Desktop and inspect the design results.
