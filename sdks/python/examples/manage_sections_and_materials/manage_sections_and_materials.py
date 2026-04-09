"""
Example: Manage Sections and Materials

Demonstrates how to:
  1. Create a new blank SPACE GASS project
  2. Create a user-defined material (structural steel)
  3. Create a user-defined section (rectangular hollow section)
  4. List all sections and materials
  5. Update a section's properties
  6. Create a member that uses the section and material
  7. Delete a section

Prerequisites:
  - SPACE GASS API running locally (default: http://localhost:5000)
  - A valid API key
"""

import asyncio
import sys

from extensions.client_extensions import create_client
from space_gass_api.models.material_create import MaterialCreate
from space_gass_api.models.member_create import MemberCreate
from space_gass_api.models.node_create import NodeCreate
from space_gass_api.models.section_create import SectionCreate
from space_gass_api.models.section_update import SectionUpdate


async def main() -> int:
    client = create_client()

    try:
        # -- Create a new blank project --------------------------------
        print("Creating new blank project...")
        await client.job.new.post()
        print("New project created.")
        print()

        # == MATERIALS =================================================

        # -- Create a structural steel material ------------------------
        print("Creating materials...")

        steel = await client.job.structure.materials.post(
            MaterialCreate(
                name="350 Grade Steel",
                youngs_modulus=200000.0,    # MPa
                poissons_ratio=0.3,
                mass_density=7850.0,        # kg/m^3
                thermal_coeff=1.17e-5,      # per degree C
            ),
        )
        print(f"  Material {steel.key}: {steel.name}")
        print(f"    Young's Modulus:  {steel.youngs_modulus} MPa")
        print(f"    Poisson's Ratio:  {steel.poissons_ratio}")
        print(f"    Mass Density:     {steel.mass_density} kg/m^3")
        print(f"    Thermal Coeff:    {steel.thermal_coeff}")
        print(f"    Source:           {steel.source}")
        print()

        # -- Create a concrete material --------------------------------
        concrete = await client.job.structure.materials.post(
            MaterialCreate(
                name="40 MPa Concrete",
                youngs_modulus=32800.0,     # MPa
                poissons_ratio=0.2,
                mass_density=2400.0,        # kg/m^3
                thermal_coeff=1.0e-5,
                concrete_strength=40.0,     # MPa
            ),
        )
        print(f"  Material {concrete.key}: {concrete.name}")
        print(f"    Concrete Strength: {concrete.concrete_strength} MPa")
        print()

        # == SECTIONS ==================================================

        # -- Create a rectangular hollow section (RHS) -----------------
        print("Creating sections...")

        rhs = await client.job.structure.sections.post(
            SectionCreate(
                name="200x100x6 RHS",
                mark="RHS",
                a=3360.0,       # mm^2  - cross-sectional area
                j=22.5e6,       # mm^4  - torsion constant
                iy=27.0e6,      # mm^4  - second moment of area (Y)
                iz=9.6e6,       # mm^4  - second moment of area (Z)
                ay=2400.0,      # mm^2  - shear area (Y)
                az=1200.0,      # mm^2  - shear area (Z)
            ),
        )
        print(f"  Section {rhs.key}: {rhs.name}")
        print(f"    A  = {rhs.a} mm^2")
        print(f"    Iy = {rhs.iy} mm^4")
        print(f"    Iz = {rhs.iz} mm^4")
        print(f"    Source: {rhs.source}")
        print()

        # -- Create a second section (circular hollow) -----------------
        chs = await client.job.structure.sections.post(
            SectionCreate(
                name="168.3x6 CHS",
                mark="CHS",
                a=3060.0,       # mm^2
                j=13.5e6,       # mm^4
                iy=6.75e6,      # mm^4
                iz=6.75e6,      # mm^4
                ay=1530.0,      # mm^2
                az=1530.0,      # mm^2
            ),
        )
        print(f"  Section {chs.key}: {chs.name}")
        print()

        # == LIST ======================================================

        # -- List all materials ----------------------------------------
        print("Listing all materials...")
        materials = await client.job.structure.materials.get()
        for mat in materials:
            print(f"  [{mat.key}] {mat.name} (E={mat.youngs_modulus}, Source={mat.source})")
        print()

        # -- List all sections -----------------------------------------
        print("Listing all sections...")
        sections = await client.job.structure.sections.get()
        for sec in sections:
            print(f"  [{sec.key}] {sec.name} (A={sec.a}, Iy={sec.iy}, Source={sec.source})")
        print()

        # == UPDATE ====================================================

        # -- Update the RHS section's area (partial update) ------------
        print(f"Updating section {rhs.key} area...")
        updated = await client.job.structure.sections.by_key(rhs.key).patch(
            SectionUpdate(
                a=3500.0,       # Increased area
                name="200x100x6.3 RHS",
            ),
        )
        print(f"  Section {updated.key}: {updated.name}")
        print(f"    A  = {updated.a} mm^2 (was {rhs.a})")
        print()

        # == CREATE MEMBER USING SECTION & MATERIAL ====================

        # -- Create nodes and a member that references our properties --
        print("Creating a beam using the new section and material...")

        node_a = await client.job.structure.nodes.post(
            NodeCreate(x=0.0, y=0.0, z=0.0),
        )
        node_b = await client.job.structure.nodes.post(
            NodeCreate(x=5.0, y=0.0, z=0.0),
        )

        member = await client.job.structure.members.post(
            MemberCreate(
                node_a=node_a.key,
                node_b=node_b.key,
                section=rhs.key,
                material=steel.key,
            ),
        )
        print(f"  Member {member.key}: Node {member.node_a} -> Node {member.node_b}")
        print(f"    Section:  {member.section}")
        print(f"    Material: {member.material}")
        print()

        # == DELETE =====================================================

        # -- Delete the unused CHS section -----------------------------
        print(f"Deleting unused section {chs.key} ({chs.name})...")
        await client.job.structure.sections.by_key(chs.key).delete()
        print("  Deleted.")
        print()

        # -- Verify deletion -------------------------------------------
        print("Remaining sections:")
        remaining = await client.job.structure.sections.get()
        for sec in remaining:
            print(f"  [{sec.key}] {sec.name}")
        print()

        # == SUMMARY ===================================================
        print("Example completed successfully!")
        print(f"  Materials created: {steel.key} ({steel.name}), {concrete.key} ({concrete.name})")
        print(f"  Sections created:  {rhs.key} ({updated.name})")
        print(f"  Members created:   {member.key}")

        # -- Close without saving (example only) -----------------------
        print()
        print("Closing project (not saving)...")
        await client.job.close.post()
        print("Done.")

    except Exception as ex:
        print(f"Error: {ex}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
