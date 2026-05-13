# Example.GeodesicDome

Builds a parametric geodesic hemisphere using bulk creation endpoints for nodes, members, and restraints. No loads or analysis — just pure geometry generation.

Adjust `Radius`, `Frequency`, and `SectionName` at the top of `Program.cs` to change the dome.

## Run it

1. Start the SPACE GASS API service.
2. From this folder:
   ```
   dotnet run
   ```

The example saves the model to `~/Desktop/SpaceGass Examples/GeodesicDome.sg` so you can open it in SPACE GASS Desktop and verify the geometry visually.
