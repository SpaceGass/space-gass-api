# manage_sections_and_materials

Walks through CRUD on sections and materials in a fresh project: create a steel material and a 40 MPa concrete material, create a user-defined RHS section and a CHS section, list everything, patch a section's properties, attach the section + material to a member, then delete the unused section.

Useful as a reference for any code that needs to populate or modify a model's sections/materials catalogue.

## Run it

1. Start the SPACE GASS API service.
2. Install dependencies:
   ```
   pip install space-gass-api
   ```
3. From this folder:
   ```
   python manage_sections_and_materials.py
   ```

The example does not save — it closes the job at the end without persisting.
