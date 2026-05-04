"""
Example: Create a Simple Beam Model from Scratch

Mirrors the Simple Beam walkthrough in the Zudoku docs site:
   1.  Create the client and a new project
   2.  Create the two nodes
   3.  Apply restraints (fixed + pinned)
   4.  Add a material
   5.  Add a library section
   6.  Create the member, wired to the section + material
   7.  Create three primary load cases (self-weight, dead, live)
   8.  Apply the self-weight load
   9.  Apply a member distributed load to the dead case
   10. Apply a member distributed load to the live case
   11. Define ULS and SLS combinations to AS/NZS 1170
   12. Run a linear static analysis and wait for completion
   13. Query reactions under the ULS combination
   14. Get the maximum ULS bending moment along the beam
   15. Get the maximum SLS deflection along the beam
   16. Save and close

Prerequisites:
  - SPACE GASS API running locally (default: http://localhost:34560)
  - The "Aust300" section library installed (default in SPACE GASS)
"""

import asyncio
import os
import sys

from kiota_abstractions.base_request_configuration import RequestConfiguration

from extensions.client_extensions import create_client
from space_gass_api.models.analysis_run_status import AnalysisRunStatus
from space_gass_api.models.combination_case_create import CombinationCaseCreate
from space_gass_api.models.combination_item import CombinationItem
from space_gass_api.models.load_case_create import LoadCaseCreate
from space_gass_api.models.load_position_units import LoadPositionUnits
from space_gass_api.models.material_create import MaterialCreate
from space_gass_api.models.member_create import MemberCreate
from space_gass_api.models.member_distributed_load_create import MemberDistributedLoadCreate
from space_gass_api.models.node_create import NodeCreate
from space_gass_api.models.node_restraint_create import NodeRestraintCreate
from space_gass_api.models.save_job_request import SaveJobRequest
from space_gass_api.models.section_library_create import SectionLibraryCreate
from space_gass_api.models.self_weight_load_create import SelfWeightLoadCreate
from space_gass_api.models.static_settings_update import StaticSettingsUpdate

from space_gass_api.job.query.analysis.static.member.intermediate_forces.intermediate_forces_request_builder import IntermediateForcesRequestBuilder
from space_gass_api.job.query.analysis.static.member.intermediate_displacements.intermediate_displacements_request_builder import IntermediateDisplacementsRequestBuilder
from space_gass_api.job.query.analysis.static.node.reactions.reactions_request_builder import ReactionsRequestBuilder

# -- Configuration ------------------------------------------------
save_file_path = os.path.join(
    os.path.expanduser("~/Desktop"),
    "SpaceGass Examples",
    "SimpleBeam.sg",
)


async def main() -> int:
    client = create_client()

    try:
        # == Step 1 — Create a new blank project =======================
        print("Creating new blank project...")
        await client.job.new.post()
        print("New project created.")
        print()

        # == Step 2 — Create nodes =====================================
        print("Creating nodes...")

        node1 = await client.job.structure.nodes.post(
            NodeCreate(x=0.0, y=0.0, z=0.0),
        )
        print(f"  Node {node1.id}: ({node1.x}, {node1.y}, {node1.z})")

        node2 = await client.job.structure.nodes.post(
            NodeCreate(x=6.0, y=0.0, z=0.0),
        )
        print(f"  Node {node2.id}: ({node2.x}, {node2.y}, {node2.z})")
        print()

        # == Step 3 — Apply restraints =================================
        # Restraint code: 6 characters for TX, TY, TZ, RX, RY, RZ
        #   F = Free, R = Restrained
        print("Applying restraints...")

        await client.job.structure.nodes.by_id(node1.id).restraint.post(
            NodeRestraintCreate(restraint_code="RRRRRR"),
        )
        print(f"  Node {node1.id}: Fixed (RRRRRR)")

        await client.job.structure.nodes.by_id(node2.id).restraint.post(
            NodeRestraintCreate(restraint_code="RRRFFF"),
        )
        print(f"  Node {node2.id}: Pinned (RRRFFF)")
        print()

        # == Step 4 — Add a material ===================================
        print("Creating material...")
        steel = await client.job.structure.materials.post(
            MaterialCreate(
                name="350 Grade Steel",
                youngs_modulus=200000.0,    # MPa
                poissons_ratio=0.3,
                mass_density=7850.0,        # kg/m^3
                thermal_coeff=1.17e-5,      # per °C
            ),
        )
        print(f"  Material {steel.id}: {steel.name}")
        print()

        # == Step 5 — Add a library section ============================
        print("Adding library section...")
        section = await client.job.structure.sections.library.post(
            SectionLibraryCreate(
                library="Aust300",
                name="360 UB 44.7",
                mark="B1",
            ),
        )
        print(f"  Section {section.id}: {section.name}")
        print()

        # == Step 6 — Create the member ================================
        print("Creating beam member...")
        member = await client.job.structure.members.post(
            MemberCreate(
                node_a=node1.id,
                node_b=node2.id,
                section=section.id,
                material=steel.id,
            ),
        )
        print(f"  Member {member.id}: Node {member.node_a} -> Node {member.node_b}")
        print()

        # == Step 7 — Create primary load cases ========================
        print("Creating primary load cases...")
        self_weight_case = await client.job.loads.load_cases.post(
            LoadCaseCreate(id=1, title="Self-weight"))
        dead_case = await client.job.loads.load_cases.post(
            LoadCaseCreate(id=2, title="Dead Load"))
        live_case = await client.job.loads.load_cases.post(
            LoadCaseCreate(id=3, title="Live Load"))
        print(f"  Cases: SW={self_weight_case.id}, G={dead_case.id}, Q={live_case.id}")
        print()

        # == Step 8 — Apply the self-weight load =======================
        print("Applying self-weight load...")
        await client.job.loads.self_weight_loads.by_case_id(self_weight_case.id).post(
            SelfWeightLoadCreate(
                acceleration_x=0.0,
                acceleration_y=-9.81,    # m/s² downward
                acceleration_z=0.0,
            ),
        )
        print()

        # == Step 9 — Member distributed load on the dead case =========
        print("Applying 2 kN/m dead load across the span...")
        await client.job.loads.member_distributed_loads.post(
            MemberDistributedLoadCreate(
                case=dead_case.id,
                member=member.id,
                position_units=LoadPositionUnits.Percent,
                start_position=0.0,
                finish_position=100.0,
                fy_start=-2.0,    # kN/m downward
                fy_finish=-2.0,
            ),
        )
        print()

        # == Step 10 — Member distributed load on the live case ========
        print("Applying 5 kN/m live load across the span...")
        await client.job.loads.member_distributed_loads.post(
            MemberDistributedLoadCreate(
                case=live_case.id,
                member=member.id,
                position_units=LoadPositionUnits.Percent,
                start_position=0.0,
                finish_position=100.0,
                fy_start=-5.0,
                fy_finish=-5.0,
            ),
        )
        print()

        # == Step 11 — ULS and SLS combinations ========================
        # Combination cases now POST as a single CombinationCaseCreate with
        # combination_items inline — one call per combination, no follow-up
        # PUT to set the items.
        print("Defining ULS and SLS combinations to AS/NZS 1170...")

        uls_case = await client.job.loads.combination_load_cases.post(
            CombinationCaseCreate(
                id=10,
                title="ULS - Strength",
                # ULS: 1.2 G + 1.5 Q (self-weight + dead are both G)
                combination_items=[
                    CombinationItem(case=self_weight_case.id, multiplying_factor=1.2),
                    CombinationItem(case=dead_case.id,        multiplying_factor=1.2),
                    CombinationItem(case=live_case.id,        multiplying_factor=1.5),
                ],
            ),
        )

        sls_case = await client.job.loads.combination_load_cases.post(
            CombinationCaseCreate(
                id=20,
                title="SLS - Short-term Deflection",
                # SLS short-term: 1.0 G + 0.7 Q
                combination_items=[
                    CombinationItem(case=self_weight_case.id, multiplying_factor=1.0),
                    CombinationItem(case=dead_case.id,        multiplying_factor=1.0),
                    CombinationItem(case=live_case.id,        multiplying_factor=0.7),
                ],
            ),
        )

        print(f"  ULS  case Id = {uls_case.id}")
        print(f"  SLS  case Id = {sls_case.id}")
        print()

        # == Step 12 — Run a linear static analysis ====================
        print("Running linear static analysis...")
        run = await client.job.analysis.static.run_linear.post(
            StaticSettingsUpdate())
        print(f"  Run {run.run_id} queued; waiting for completion...")

        while True:
            await asyncio.sleep(0.5)
            final_run = await client.job.analysis.runs.by_run_id(run.run_id).get()
            if final_run.status in (
                AnalysisRunStatus.Completed,
                AnalysisRunStatus.Failed,
                AnalysisRunStatus.Cancelled,
            ):
                break

        print(f"  Analysis {final_run.status} in {final_run.elapsed_time}")
        if final_run.status != AnalysisRunStatus.Completed:
            raise RuntimeError(
                f"Analysis did not complete: {final_run.error_message}")
        print()

        # == Step 13 — Query reactions =================================
        print("Querying ULS reactions...")
        reaction_params = ReactionsRequestBuilder.ReactionsRequestBuilderGetQueryParameters(
            cases=str(uls_case.id))
        reactions = await client.job.query.analysis.static.node.reactions.get(
            request_configuration=RequestConfiguration(query_parameters=reaction_params))

        if reactions.warnings and reactions.warnings.cases_not_analyzed:
            raise RuntimeError(
                f"Cases not analysed: {reactions.warnings.cases_not_analyzed}. "
                "Run the analysis first.")

        for r in reactions.results:
            print(
                f"  Node {r.node}, LC {r.case}: "
                f"Fx={r.fx:.2f}, Fy={r.fy:.2f}, Fz={r.fz:.2f}")
        print()

        # == Step 14 — Maximum ULS bending moment ======================
        force_params = IntermediateForcesRequestBuilder.IntermediateForcesRequestBuilderGetQueryParameters(
            cases=str(uls_case.id),
            members=str(member.id))
        uls_forces = await client.job.query.analysis.static.member.intermediate_forces.get(
            request_configuration=RequestConfiguration(query_parameters=force_params))

        beam_forces = uls_forces.results[0]
        max_mz = max(abs(v) for v in beam_forces.mz if v is not None)
        print(f"Max ULS bending moment on Member {member.id}: {max_mz:.2f} kNm")

        # == Step 15 — Maximum SLS deflection ==========================
        displ_params = IntermediateDisplacementsRequestBuilder.IntermediateDisplacementsRequestBuilderGetQueryParameters(
            cases=str(sls_case.id),
            members=str(member.id))
        sls_displacements = await client.job.query.analysis.static.member.intermediate_displacements.get(
            request_configuration=RequestConfiguration(query_parameters=displ_params))

        beam_displacements = sls_displacements.results[0]
        max_deflection = max(abs(v) for v in beam_displacements.ty_global if v is not None)
        print(f"Max SLS deflection on Member {member.id}: {max_deflection * 1000:.2f} mm")
        print()

        # == Step 16 — Save and close ==================================
        print(f"Saving project to: {save_file_path}")
        await client.job.save.post(
            SaveJobRequest(file_path=save_file_path),
        )
        print("Project saved.")

        print("Closing project...")
        await client.job.close.post()
        print("Project closed.")

    except Exception as ex:
        print(f"Error: {ex}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
