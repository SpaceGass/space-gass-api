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
  - SPACE GASS API running locally (default: http://localhost:34560)
"""

import asyncio
import sys

from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models


async def main() -> int:
    client = SpaceGassApiClient.create_client("http://localhost:34560")

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
            models.MaterialUserCreate(
                name="350 Grade Steel",
                youngs_modulus=200000.0,    # MPa
                poissons_ratio=0.3,
                mass_density=7850.0,        # kg/m^3
                thermal_coeff=1.17e-5,      # per degree C
            ),
        )
        print(f"  Material {steel.id}: {steel.name}")
        print(f"    Young's Modulus:  {steel.youngs_modulus} MPa")
        print(f"    Poisson's Ratio:  {steel.poissons_ratio}")
        print(f"    Mass Density:     {steel.mass_density} kg/m^3")
        print(f"    Thermal Coeff:    {steel.thermal_coeff}")
        print(f"    Source:           {steel.source}")
        print()

        # -- Create a concrete material --------------------------------
        concrete = await client.job.structure.materials.post(
            models.MaterialUserCreate(
                name="40 MPa Concrete",
                youngs_modulus=32800.0,     # MPa
                poissons_ratio=0.2,
                mass_density=2400.0,        # kg/m^3
                thermal_coeff=1.0e-5,
                concrete_strength=40.0,     # MPa
            ),
        )
        print(f"  Material {concrete.id}: {concrete.name}")
        print(f"    Concrete Strength: {concrete.concrete_strength} MPa")
        print()

        # == SECTIONS ==================================================

        # -- Create a rectangular hollow section (RHS) -----------------
        print("Creating sections...")

        rhs = await client.job.structure.sections.post(
            models.SectionUserCreate(
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
        print(f"  Section {rhs.id}: {rhs.name}")
        print(f"    A  = {rhs.a} mm^2")
        print(f"    Iy = {rhs.iy} mm^4")
        print(f"    Iz = {rhs.iz} mm^4")
        print(f"    Source: {rhs.source}")
        print()

        # -- Create a second section (circular hollow) -----------------
        chs = await client.job.structure.sections.post(
            models.SectionUserCreate(
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
        print(f"  Section {chs.id}: {chs.name}")
        print()

        # == LIST ======================================================

        # -- List all materials ----------------------------------------
        print("Listing all materials...")
        materials = await client.job.structure.materials.get()
        for mat in materials:
            print(f"  [{mat.id}] {mat.name} (E={mat.youngs_modulus}, Source={mat.source})")
        print()

        # -- List all sections -----------------------------------------
        print("Listing all sections...")
        sections = await client.job.structure.sections.get()
        for sec in sections:
            print(f"  [{sec.id}] {sec.name} (A={sec.a}, Iy={sec.iy}, Source={sec.source})")
        print()

        # == UPDATE ====================================================

        # -- Update the RHS section's area (partial update) ------------
        print(f"Updating section {rhs.id} area...")
        updated = await client.job.structure.sections.by_id(rhs.id).patch(
            models.SectionUpdate(
                a=3500.0,       # Increased area
                name="200x100x6.3 RHS",
            ),
        )
        print(f"  Section {updated.id}: {updated.name}")
        print(f"    A  = {updated.a} mm^2 (was {rhs.a})")
        print()

        # == CREATE MEMBER USING SECTION & MATERIAL ====================

        # -- Create nodes and a member that references our properties --
        print("Creating a beam using the new section and material...")

        node_a = await client.job.structure.nodes.post(
            models.NodeCreate(x=0.0, y=0.0, z=0.0),
        )
        node_b = await client.job.structure.nodes.post(
            models.NodeCreate(x=5.0, y=0.0, z=0.0),
        )

        member = await client.job.structure.members.post(
            models.MemberCreate(
                node_a=node_a.id,
                node_b=node_b.id,
                section=rhs.id,
                material=steel.id,
            ),
        )
        print(f"  Member {member.id}: Node {member.node_a} -> Node {member.node_b}")
        print(f"    Section:  {member.section}")
        print(f"    Material: {member.material}")
        print()

        # == DELETE =====================================================

        # -- Delete the unused CHS section -----------------------------
        print(f"Deleting unused section {chs.id} ({chs.name})...")
        await client.job.structure.sections.by_id(chs.id).delete()
        print("  Deleted.")
        print()

        # -- Verify deletion -------------------------------------------
        print("Remaining sections:")
        remaining = await client.job.structure.sections.get()
        for sec in remaining:
            print(f"  [{sec.id}] {sec.name}")
        print()

        # == SUMMARY ===================================================
        print("Example completed successfully!")
        print(f"  Materials created: {steel.id} ({steel.name}), {concrete.id} ({concrete.name})")
        print(f"  Sections created:  {rhs.id} ({updated.name})")
        print(f"  Members created:   {member.id}")

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
