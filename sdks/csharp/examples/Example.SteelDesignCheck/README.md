# Example.SteelDesignCheck

Builds the simply-supported beam from `Example.CreateSimpleBeam`, analyses it, then runs a steel member design **CHECK** to AS 4100: lists the design codes this seat is licensed for, creates a steel member design group, sets the general and AS 4100 settings, starts the check run, polls it to completion and prints the check summary for the design group (load factor, critical case, failure mode).

A check verifies the members' current sections without changing the model. See `Example.SteelDesignOptimise` for a DESIGN run that selects new sections.

The loads are applied in global Y, so the results assume the vertical axis is set to Y in SPACE GASS preferences.

## Run it

1. Start the SPACE GASS API service (a licence for the AS 4100 steel member design module is required).
2. From this folder:
   ```
   dotnet run
   ```

The example saves the model to `Desktop/SpaceGass Examples/SteelDesignCheck.sg` so you can open it in SPACE GASS Desktop and inspect the design results.
