"""
Example: Create a Built-up Section with the Shape Builder

Builds a compound section — a 360 UB 44.7 with a 250 x 16 cover plate
welded to its top flange — and applies it to a simply-supported beam:
   1.  Create the client and a new project
   2.  Nodes, restraints and material for a 6 m beam
   3.  Preview the bare UB to see its numbered reference points
   4.  Define the plate, anchored onto the UB's top-centre point
   5.  Preview the compound section (nothing is written yet)
   6.  Create the section — SPACE GASS computes A, J, Iy, Iz
   7.  Compare with the plain library UB
   8.  Create the beam member on the built-up section
   9.  Read the section back and list its shapes
   10. Save and close

Shape-builder sections hold up to 20 shapes. A shape is either drawn
from dimensions (IShape, RectangularBarShape, ChannelShape, ...) or
taken from a section library (LibraryShape). Dimensions and translations
are in the job's section-properties unit (mm by default); see
GET /job/units.

Prerequisites:
  - SPACE GASS API running locally (default: http://localhost:34560)
  - The "Aust300" section library installed (default in SPACE GASS)
"""

import asyncio
import os
import sys
import winreg

from space_gass_api import SpaceGassApiClient, shape_builder
import space_gass_api.models as models

# -- Configuration ------------------------------------------------
with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders") as _k:
    _DESKTOP = winreg.QueryValueEx(_k, "Desktop")[0]

save_file_path = os.path.join(_DESKTOP, "SpaceGass Examples-py", "BuiltUpSection.sg")


async def main() -> int:
    client = SpaceGassApiClient.create_client("http://localhost:34560")

    try:
        # == Step 1 — Create a new blank project =======================
        print("Creating new blank project...")
        await client.job.new.post()

        units = await client.job.units.get()
        print(f"  Section dimensions are in {units.section_properties}.")
        print()

        # == Step 2 — Nodes, restraints and material ===================
        print("Creating nodes, restraints and material...")

        node1 = await client.job.structure.nodes.post(models.NodeCreate(x=0.0, y=0.0, z=0.0))
        node2 = await client.job.structure.nodes.post(models.NodeCreate(x=6.0, y=0.0, z=0.0))

        await client.job.structure.node_restraints.post(
            models.NodeRestraintCreate(node=node1.id, restraint_code="FFFFFF"))
        await client.job.structure.node_restraints.post(
            models.NodeRestraintCreate(node=node2.id, restraint_code="FFFRRR"))

        steel = await client.job.structure.materials.library.post(
            models.MaterialLibraryCreate(library="Aust", name="STEEL"))
        print()

        # == Step 3 — Preview the bare UB ==============================
        # The preview endpoint computes the geometry a shape-builder body
        # would produce without writing anything. Each shape comes back
        # with its extent and numbered reference points — the points an
        # anchor_position refers to when snapping shapes together.
        #
        # shape_builder.shapes(...) takes plain shape objects; Kiota's
        # per-shape wrapper and the shape_type discriminator are handled.
        print("Previewing the bare 360 UB 44.7...")
        ub = models.LibraryShape(library="Aust300", name="360 UB 44.7")

        ub_preview = await client.job.structure.sections.shape_builder.preview.post(
            models.SectionShapeBuilderCreate(name="UB only", shapes=shape_builder.shapes(ub)))

        ub_geometry = ub_preview.shapes[0]
        print(f"  Depth {ub_geometry.bounds.min_y} .. {ub_geometry.bounds.max_y}, "
              f"width {ub_geometry.bounds.min_z} .. {ub_geometry.bounds.max_z}")
        print("  Reference points (point: y, z):")
        for p in ub_geometry.reference_points[:5]:
            print(f"    {p.point}: {p.y}, {p.z}")
        print("    ...")

        # Point 1 is the centroid; points 2-5 are the top, right, bottom and
        # left mid-edges. Pick the top-centre point by its geometry rather
        # than assuming a number.
        ub_top_centre = max(
            (p for p in ub_geometry.reference_points if p.z == 0),
            key=lambda p: p.y)
        print(f"  Top-centre of the UB is reference point {ub_top_centre.point}.")
        print()

        # == Step 4 — Define the cover plate ===========================
        # A 250 wide x 16 thick plate. Its bottom-centre point (4) snaps
        # onto the UB's top-centre point, so it sits flush on the flange.
        # anchor_position is input-only: the API converts it to
        # translate_y / translate_z, which is what you get back.
        print("Defining the 250 x 16 cover plate...")
        plate = models.RectangularBarShape(
            d=16.0,
            b=250.0,
            fabrication=models.ShapeFabrication.Heavily_Welded,
            anchor_position=models.ShapeAnchorPosition(
                anchor_shape=1,                     # the UB (one-based position in shapes)
                anchor_point=ub_top_centre.point,   # ... its top-centre point
                shape_point=4,                      # the plate's bottom-centre point
            ),
        )
        print()

        # == Step 5 — Preview the compound section =====================
        request = models.SectionShapeBuilderCreate(
            name="360 UB 44.7 + 250x16 plate",
            mark="B1",
            shapes=shape_builder.shapes(ub, plate),
        )

        print("Previewing the compound section...")
        preview = await client.job.structure.sections.shape_builder.preview.post(request)
        print(f"  Overall depth {preview.bounds.max_y - preview.bounds.min_y}, "
              f"width {preview.bounds.max_z - preview.bounds.min_z}")
        for s in preview.shapes:
            print(f"  Shape {s.shape}: y {s.bounds.min_y:.1f} .. {s.bounds.max_y:.1f}")
        print()

        # == Step 6 — Create the section ===============================
        # Same body as the preview. SPACE GASS computes the structural
        # properties from the shapes — the caller never supplies them.
        print("Creating the built-up section...")
        built_up = await client.job.structure.sections.shape_builder.post(request)
        print(f"  Section {built_up.id}: {built_up.name} ({built_up.shape_count} shapes)")
        print()

        # == Step 7 — Compare with the plain UB ========================
        plain_ub = await client.job.structure.sections.library.post(
            models.SectionLibraryCreate(library="Aust300", name="360 UB 44.7", mark="B0"))

        print(f"  {'Property':<10} {'360 UB 44.7':>14} {'UB + plate':>14}")
        print(f"  {'A':<10} {plain_ub.a:>14.0f} {built_up.a:>14.0f}")
        print(f"  {'Iy':<10} {plain_ub.iy:>14.3e} {built_up.iy:>14.3e}")
        print(f"  {'Iz':<10} {plain_ub.iz:>14.3e} {built_up.iz:>14.3e}")
        print(f"  {'J':<10} {plain_ub.j:>14.3e} {built_up.j:>14.3e}")
        print()

        # == Step 8 — Create the beam member ===========================
        print("Creating beam member on the built-up section...")
        member = await client.job.structure.members.post(
            models.MemberCreate(
                node_a=node1.id,
                node_b=node2.id,
                section=built_up.id,
                material=steel.id,
            ))
        print(f"  Member {member.id}: section {member.section}")
        print()

        # == Step 9 — Read the section back ============================
        # GET /sections/{id} expands the shapes by default.
        # shape_builder.shapes_of() unwraps them to typed shape objects.
        print("Reading the section back...")
        saved = await client.job.structure.sections.by_id(built_up.id).get()
        # A LibraryShape is resolved on create: it comes back as the
        # concrete shape (here an IShape) carrying the library item's name.
        for shape in shape_builder.shapes_of(saved):
            if isinstance(shape, models.IShape):
                detail = f"{shape.d} deep x {shape.bt} wide"
            elif isinstance(shape, models.RectangularBarShape):
                detail = f"{shape.b} x {shape.d}"
            else:
                detail = ""
            print(f"  Shape {shape.id}: {shape.shape_type:<15} {shape.shape_name or '':<14} {detail:<20} "
                  f"translate_y={shape.translate_y} translate_z={shape.translate_z}")
        print()

        # == Step 10 — Save and close ==================================
        print(f"Saving model to: {save_file_path}")
        await client.job.save.post(models.SaveJobRequest(file_path=save_file_path))
        print("Project saved.")

    except models.ErrorResponse as err:
        print(f"API error {err.status}: {err.title}", file=sys.stderr)
        if err.detail:
            print(f"  {err.detail}", file=sys.stderr)
        if err.error_code:
            print(f"  Code: {err.error_code}", file=sys.stderr)
        for ve in err.errors or []:
            print(f"  [{ve.field}] {ve.message}", file=sys.stderr)
        return 1
    except Exception as ex:
        print(f"Error: {ex}", file=sys.stderr)
        return 1

    finally:
        # Always close the active job so the next run starts clean.
        try:
            print("Closing project...")
            await client.job.close.post()
            print("Project closed.")
        except Exception as close_ex:
            print(f"Warning: failed to close job: {close_ex}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
