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
   12. Save the initial model (so you can open it in SPACE GASS to verify)
   13. Configure the static analysis settings (solver, optimisation)
   14. Run a linear static analysis and wait for completion
   15. Query reactions under the ULS combination
   16. Get the maximum ULS bending moment along the beam
   17. Get the maximum SLS deflection along the beam
   18. Save the analysed model and close

Prerequisites:
  - SPACE GASS API running locally (default: http://localhost:34560)
  - The "Aust300" section library installed (default in SPACE GASS)
"""

import asyncio
import os
import sys
import winreg

from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models
from space_gass_api.utils import to_filter_string

# -- Configuration ------------------------------------------------
with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders") as _k:
    _DESKTOP = winreg.QueryValueEx(_k, "Desktop")[0]

save_file_path = os.path.join(_DESKTOP, "SpaceGass Examples-py", "SimpleBeam.sg")


async def main() -> int:
    client = SpaceGassApiClient.create_client("http://localhost:34560")

    try:
        # == Step 1 — Create a new blank project =======================
        print("Creating new blank project...")
        await client.job.new.post()
        print("New project created.")
        print()

        # == Step 2 — Create nodes =====================================
        print("Creating nodes...")

        node1 = await client.job.structure.nodes.post(
            models.NodeCreate(x=0.0, y=0.0, z=0.0),
        )
        print(f"  Node {node1.id}: ({node1.x}, {node1.y}, {node1.z})")

        node2 = await client.job.structure.nodes.post(
            models.NodeCreate(x=6.0, y=0.0, z=0.0),
        )
        print(f"  Node {node2.id}: ({node2.x}, {node2.y}, {node2.z})")
        print()

        # == Step 3 — Apply restraints =================================
        # Restraint code: 6 characters for TX, TY, TZ, RX, RY, RZ
        #   F = Fixed (prevents movement)
        #   R = Released (allows movement)
        #   S = Spring (governed by a spring stiffness)
        #   V = Variable spring (stiffness-vs-deflection table)
        #   P = Plastic (upper force/moment limit on the reaction)
        #   N = Friction (limit proportional to the normal-axis reaction)
        print("Applying restraints...")

        await client.job.structure.node_restraints.post(
            models.NodeRestraintCreate(node=node1.id, restraint_code="FFFFFF"),
        )
        print(f"  Node {node1.id}: Fixed (FFFFFF)")

        await client.job.structure.node_restraints.post(
            models.NodeRestraintCreate(node=node2.id, restraint_code="FFFRRR"),
        )
        print(f"  Node {node2.id}: Pinned (FFFRRR)")
        print()

        # == Step 4 — Add a library material ===========================
        print("Adding library material...")
        steel = await client.job.structure.materials.library.post(
            models.MaterialLibraryCreate(
                library="Aust",
                name="STEEL",
            ),
        )
        print(f"  Material {steel.id}: {steel.name}")
        print()

        # == Step 5 — Add a library section ============================
        print("Adding library section...")
        section = await client.job.structure.sections.library.post(
            models.SectionLibraryCreate(
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
            models.MemberCreate(
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
            models.LoadCaseCreate(id=1, title="Self-weight"))
        dead_case = await client.job.loads.load_cases.post(
            models.LoadCaseCreate(id=2, title="Dead Load"))
        live_case = await client.job.loads.load_cases.post(
            models.LoadCaseCreate(id=3, title="Live Load"))
        print(f"  Cases: SW={self_weight_case.id}, G={dead_case.id}, Q={live_case.id}")
        print()

        # == Step 8 — Apply the self-weight load =======================
        print("Applying self-weight load...")
        await client.job.loads.self_weight_loads.post(
            models.SelfWeightLoadCreate(
                load_case=self_weight_case.id,
                acceleration_x=0.0,
                acceleration_y=-1.0,    # 1 G downward
                acceleration_z=0.0,
            ),
        )
        print()

        # == Step 9 — Member distributed load on the dead case =========
        print("Applying 2 kN/m dead load across the span...")
        await client.job.loads.member_distributed_loads.post(
            models.MemberDistributedLoadCreate(
                load_case=dead_case.id,
                member=member.id,
                position_units=models.LoadPositionUnits.Percent,
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
            models.MemberDistributedLoadCreate(
                load_case=live_case.id,
                member=member.id,
                position_units=models.LoadPositionUnits.Percent,
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
            models.CombinationLoadCaseCreate(
                id=10,
                title="ULS - Strength",
                # ULS: 1.2 G + 1.5 Q (self-weight + dead are both G)
                combination_items=[
                    models.CombinationLoadCaseItem(load_case=self_weight_case.id, multiplying_factor=1.2),
                    models.CombinationLoadCaseItem(load_case=dead_case.id,        multiplying_factor=1.2),
                    models.CombinationLoadCaseItem(load_case=live_case.id,        multiplying_factor=1.5),
                ],
            ),
        )

        sls_case = await client.job.loads.combination_load_cases.post(
            models.CombinationLoadCaseCreate(
                id=20,
                title="SLS - Short-term Deflection",
                # SLS short-term: 1.0 G + 0.7 Q
                combination_items=[
                    models.CombinationLoadCaseItem(load_case=self_weight_case.id, multiplying_factor=1.0),
                    models.CombinationLoadCaseItem(load_case=dead_case.id,        multiplying_factor=1.0),
                    models.CombinationLoadCaseItem(load_case=live_case.id,        multiplying_factor=0.7),
                ],
            ),
        )

        print(f"  ULS  case Id = {uls_case.id}")
        print(f"  SLS  case Id = {sls_case.id}")
        print()

        # == Step 12 — Save the initial model ==========================
        # Save before running the analysis so you can open the .sg in
        # SPACE GASS and inspect the model state if anything fails.
        print(f"Saving initial model to: {save_file_path}")
        initial_save = await client.job.save.post(
            models.SaveJobRequest(file_path=save_file_path),
        )

        job_file = initial_save.state.file if initial_save and initial_save.state else None
        print(f"  Path:     {job_file.path if job_file else None}")
        print(f"  Name:     {job_file.name if job_file else None}")
        print(f"  Source:   {job_file.source if job_file else None}")
        print(f"  IsNew:    {initial_save.state.is_new if initial_save and initial_save.state else None}")
        print(f"  IsOpen:   {initial_save.state.is_open if initial_save and initial_save.state else None}")
        print()

        # == Step 13 — Configure the static analysis settings ==========
        # PATCH the stored static analysis settings before running. The
        # API currently only supports the Paradise solver, so pin
        # solver_type = Paradise here.
        print("Configuring static analysis settings...")
        await client.job.analysis.static.settings.patch(
            models.StaticSettingsUpdate(
                solver_type=models.SolverType.Paradise,
            ))

        # == Step 14 — Run a linear static analysis ====================
        print("Running linear static analysis...")
        run = await client.job.analysis.static.run_linear.post(
            models.StaticSettingsUpdate())
        print(f"  Run {run.run_id} queued; waiting for completion...")

        while True:
            await asyncio.sleep(0.5)
            final_run = await client.job.analysis.runs.by_run_id(str(run.run_id)).get()
            if final_run.status in (
                models.AnalysisRunStatus.Completed,
                models.AnalysisRunStatus.Failed,
                models.AnalysisRunStatus.Cancelled,
            ):
                break

        print(f"  Analysis {final_run.status} in {final_run.elapsed_time}")
        if final_run.status != models.AnalysisRunStatus.Completed:
            raise RuntimeError(
                f"Analysis did not complete: {final_run.error_message}")
        print()

        # == Step 15 — Query reactions =================================
        print("Querying ULS reactions...")
        reactions = await client.job.query.analysis.static.node_reactions.get(
            load_cases=to_filter_string([uls_case.id]),
        )

        if reactions.warnings and reactions.warnings.load_cases_not_analyzed:
            raise RuntimeError(
                f"Cases not analysed: {reactions.warnings.load_cases_not_analyzed}. "
                "Run the analysis first.")

        for r in reactions.results:
            print(
                f"  Node {r.node}, LC {r.load_case}: "
                f"Fx={r.fx:.2f}, Fy={r.fy:.2f}, Fz={r.fz:.2f}")
        print()

        # == Step 16 — Maximum ULS bending moment ======================
        uls_forces = await client.job.query.analysis.static.member_intermediate_forces.get(
            load_cases=to_filter_string([uls_case.id]),
            members=to_filter_string([member.id]),
        )

        beam_forces = uls_forces.results[0]
        max_mz = max(abs(v) for v in beam_forces.mz if v is not None)
        print(f"Max ULS bending moment on Member {member.id}: {max_mz:.2f} kNm")

        # == Step 17 — Maximum SLS deflection ==========================
        sls_displacements = await client.job.query.analysis.static.member_intermediate_displacements.get(
            load_cases=to_filter_string([sls_case.id]),
            members=to_filter_string([member.id]),
        )

        beam_displacements = sls_displacements.results[0]
        max_deflection = max(abs(v) for v in beam_displacements.ty_global if v is not None)
        print(f"Max SLS deflection on Member {member.id}: {max_deflection * 1000:.2f} mm")
        print()

        # == Step 18 — Save the analysed model =========================
        # Closing the job runs in `finally` below, so it always happens
        # even if a step above raised — leaving the service without a
        # half-built active job.
        print(f"Saving analysed model to: {save_file_path}")
        await client.job.save.post(
            models.SaveJobRequest(file_path=save_file_path),
        )
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
