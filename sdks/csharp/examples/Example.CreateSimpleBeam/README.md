# Example.CreateSimpleBeam

Backs the [Simple Beam tutorial](https://api.spacegass.com/docs/guides/examples/simple-beam) end-to-end. Builds a simply-supported beam from scratch, runs a linear static analysis, and queries the maximum bending moment + deflection.

The full pipeline: project → nodes → restraints → material → section → member → load cases → loads → combinations → save → analyse → query.

## Run it

1. Start the SPACE GASS API service.
2. From this folder:
   ```
   dotnet run
   ```

The example saves the model to `~/Desktop/SpaceGass Examples/SimpleBeam.sg` so you can open it in SPACE GASS Desktop and verify the geometry / results visually.
