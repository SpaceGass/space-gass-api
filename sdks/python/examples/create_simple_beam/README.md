# create_simple_beam

Backs the [Simple Beam tutorial](https://spacegass.github.io/space-gass-api/guides/examples/simple-beam) end-to-end. Builds a simply-supported beam from scratch, runs a linear static analysis, and queries the maximum bending moment + deflection.

The full pipeline: project → nodes → restraints → material → section → member → load cases → loads → combinations → save → analyse → query.

## Run it

1. Start the SPACE GASS API service.
2. Install dependencies:
   ```
   pip install space-gass-api
   ```
3. From this folder:
   ```
   python create_simple_beam.py
   ```

The example saves the model to `~/Desktop/SpaceGass Examples/SimpleBeam.sg` so you can open it in SPACE GASS Desktop and verify the geometry / results visually.
