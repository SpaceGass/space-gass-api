# geodesic_dome

Builds a parametric geodesic hemisphere using bulk creation endpoints for nodes, members, and restraints. No loads or analysis — just pure geometry generation.

Adjust `RADIUS`, `FREQUENCY`, and `SECTION_NAME` at the top of the script to change the dome.

## Run it

1. Start the SPACE GASS API service.
2. Install dependencies:
   ```
   pip install space-gass-api
   ```
3. From this folder:
   ```
   python geodesic_dome.py
   ```

The example saves the model to `~/Desktop/SpaceGass Examples-py/GeodesicDome.sg` so you can open it in SPACE GASS Desktop and verify the geometry visually.
