"""
Example: Steel Member DESIGN to AS 4100 (section selection)

Builds the same simply-supported beam as create_simple_beam, but starts
it on a deliberately heavy section, then lets a DESIGN run pick the
lightest adequate section from the section library:
   1.  Create the client and a new project
   2.  Build the beam on a 610 UB 125
   3.  Confirm which section library the design will select from
   4.  Load cases, loads and a ULS combination
   5.  Run a linear static analysis and wait for completion
   6.  Create a steel member design group (optimise for weight)
   7.  General design settings — groups and load cases
   8.  Design iteration settings — re-analyse and iterate until stable
   9.  Start the DESIGN run and poll until it finishes
   10. Report what the run did and which section it chose
   11. Query the check summary for the final section
   12. Save and close

With update_sections=True (the default) the run swaps the member's
analysis section for the selected size and, as the iteration settings
direct, re-runs the static analysis and the design until the analysis
and design sections agree. See steel_design_check for a CHECK run
that leaves the model unchanged.

Prerequisites:
  - SPACE GASS API running locally (default: http://localhost:34560)
  - The "Aust300" section library installed (default in SPACE GASS)
  - A licence for the AS 4100 steel member design module
"""

import asyncio
import os
import sys
import winreg

from space_gass_api import SpaceGassApiClient, steel_design
import space_gass_api.models as models
from space_gass_api.utils import to_filter_string

# -- Configuration ------------------------------------------------
with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders") as _k:
    _DESKTOP = winreg.QueryValueEx(_k, "Desktop")[0]

save_file_path = os.path.join(_DESKTOP, "SpaceGass Examples-py", "SteelDesignOptimise.sg")

DESIGN_CODE = steel_design.AS4100      # route segment: steel-design/{code}/...

TERMINAL = (
    models.AnalysisRunStatus.Completed,
    models.AnalysisRunStatus.Failed,
    models.AnalysisRunStatus.Cancelled,
)


async def main() -> int:
    client = SpaceGassApiClient.create_client("http://localhost:34560")

    try:
        # == Step 1 — Create a new blank project =======================
        print("Creating new blank project...")
        await client.job.new.post()
        print()

        # == Step 2 — Build the beam on a heavy section ================
        print("Building a 6 m simply-supported beam on a 610 UB 125...")

        node1 = await client.job.structure.nodes.post(models.NodeCreate(x=0.0, y=0.0, z=0.0))
        node2 = await client.job.structure.nodes.post(models.NodeCreate(x=6.0, y=0.0, z=0.0))

        await client.job.structure.node_restraints.post(
            models.NodeRestraintCreate(node=node1.id, restraint_code="FFFFFF"))
        await client.job.structure.node_restraints.post(
            models.NodeRestraintCreate(node=node2.id, restraint_code="FFFRRR"))

        steel = await client.job.structure.materials.library.post(
            models.MaterialLibraryCreate(library="Aust", name="STEEL"))

        initial_section = await client.job.structure.sections.library.post(
            models.SectionLibraryCreate(library="Aust300", name="610 UB 125", mark="B1"))

        member = await client.job.structure.members.post(
            models.MemberCreate(
                node_a=node1.id,
                node_b=node2.id,
                section=initial_section.id,
                material=steel.id,
            ))
        print(f"  Member {member.id}: {initial_section.name}")
        print()

        # == Step 3 — Where the design selects sections from ===========
        # A DESIGN run picks replacement sections from the default section
        # library nominated in SPACE GASS (Preferences > Default Libraries),
        # narrowed by the design group's scan code to compatible shapes.
        libraries = await client.job.settings.default_libraries.get()
        print(f'Design will select sections from the "{libraries.sections}" library.')
        print()

        # == Step 4 — Load cases, loads and a ULS combination ==========
        print("Applying loads and defining the ULS combination...")

        self_weight_case = await client.job.loads.load_cases.post(
            models.LoadCaseCreate(id=1, title="Self-weight"))
        dead_case = await client.job.loads.load_cases.post(
            models.LoadCaseCreate(id=2, title="Dead Load"))
        live_case = await client.job.loads.load_cases.post(
            models.LoadCaseCreate(id=3, title="Live Load"))

        await client.job.loads.self_weight_loads.post(
            models.SelfWeightLoadCreate(
                load_case=self_weight_case.id,
                acceleration_x=0.0,
                acceleration_y=-1.0,    # 1 G downward
                acceleration_z=0.0,
            ))

        await client.job.loads.member_distributed_loads.post(
            models.MemberDistributedLoadCreate(
                load_case=dead_case.id,
                member=member.id,
                position_units=models.LoadPositionUnits.Percent,
                start_position=0.0,
                finish_position=100.0,
                fy_start=-8.0,    # kN/m downward
                fy_finish=-8.0,
            ))

        await client.job.loads.member_distributed_loads.post(
            models.MemberDistributedLoadCreate(
                load_case=live_case.id,
                member=member.id,
                position_units=models.LoadPositionUnits.Percent,
                start_position=0.0,
                finish_position=100.0,
                fy_start=-10.0,
                fy_finish=-10.0,
            ))

        # ULS: 1.2 G + 1.5 Q (AS/NZS 1170.0)
        uls_case = await client.job.loads.combination_load_cases.post(
            models.CombinationLoadCaseCreate(
                id=10,
                title="ULS - Strength",
                combination_items=[
                    models.CombinationLoadCaseItem(load_case=self_weight_case.id, multiplying_factor=1.2),
                    models.CombinationLoadCaseItem(load_case=dead_case.id,        multiplying_factor=1.2),
                    models.CombinationLoadCaseItem(load_case=live_case.id,        multiplying_factor=1.5),
                ],
            ))
        print(f"  ULS case Id = {uls_case.id}")
        print()

        # == Step 5 — Run a linear static analysis =====================
        # The design run needs static results to start from. When it
        # re-analyses after swapping sections it uses the same stored
        # analysis settings, so the solver must be one the API supports.
        print("Running linear static analysis...")
        await client.job.analysis.static.settings.patch(
            models.StaticSettingsUpdate(solver_type=models.SolverType.Paradise))

        analysis_run = await client.job.analysis.static.run_linear.post(
            models.StaticSettingsUpdate())

        while True:
            await asyncio.sleep(0.5)
            final_analysis = await client.job.analysis.runs.by_run_id(analysis_run.run_id).get()
            if final_analysis.status in TERMINAL:
                break

        print(f"  Analysis {final_analysis.status.value} in {final_analysis.elapsed_time}")
        if final_analysis.status != models.AnalysisRunStatus.Completed:
            raise RuntimeError(f"Analysis did not complete: {final_analysis.error_message}")
        print()

        # == Step 6 — Create a steel member design group ===============
        print("Creating steel member design group...")
        group = await client.job.design.steel_members.post(
            models.SteelMemberCreate(
                id=1,
                description="Floor beam B1",
                members=str(member.id),
                member_type=models.SteelMemberType.Beam,
                strength_grade=models.SteelStrengthGrade.Normal,
                load_height_position=models.LoadHeightPosition.Top,
                # Compression effective lengths as actual lengths (full span,
                # pinned ends) rather than from a buckling analysis.
                length_unit_basis=models.LengthUnitBasis.Actual,
                calculate_lc_major_from_buckling=False,
                lc_major=6.0,
                calculate_lc_minor_from_buckling=False,
                lc_minor=6.0,
                calculate_lb_from_flange_restraints=True,
                # Pick the lightest adequate section rather than the shallowest.
                design_criteria=models.SteelDesignCriteria.Weight,
            ))
        print(f"  Design group {group.id}: members {group.members}, criteria {group.design_criteria.value}")
        print()

        # == Step 7 — General design settings ==========================
        # groups, load_cases (and sections, not used here) filter what the
        # run designs: which design groups, against which load cases, and —
        # via sections — only members on those section property numbers.
        print("Configuring general design settings...")
        settings = await client.job.design.steel_design.settings.patch(
            models.SteelMemberDesignGeneralSettingsUpdate(
                groups=to_filter_string([group.id]),
                load_cases=to_filter_string([uls_case.id]),
                load_factor_limit=1.0,
            ))
        print(f"  Groups: {settings.groups}, Load cases: {settings.load_cases}")
        print()

        # == Step 8 — Design iteration settings ========================
        # What happens after the run selects sections: re-run the static
        # analysis with the new sections, re-run the design, and keep
        # iterating (up to iterations times) until the design settles.
        print("Configuring design iteration settings...")
        iteration = await client.job.design.steel_design.design_iteration_settings.patch(
            models.SteelMemberDesignIterationSettingsUpdate(
                rerun_static_analysis=True,
                rerun_steel_member_design=True,
                auto_iterate=True,
                iterations=5,
            ))
        print(f"  Re-run static: {iteration.rerun_static_analysis}, "
              f"auto-iterate: {iteration.auto_iterate}, max iterations: {iteration.iterations}")
        print()

        # == Step 9 — Start the DESIGN run and poll ====================
        # update_sections=True applies the selected sections to the model.
        # Everything in the body is optional — the settings PATCHed above
        # could equally have been passed here as per-run overrides.
        print(f"Starting {DESIGN_CODE} DESIGN run...")
        design_run = await client.job.design.steel_design.by_code(DESIGN_CODE).run_design.post(
            steel_design.run_design_request(update_sections=True))
        print(f"  Run {design_run.run_id} {design_run.status.value}; waiting for completion...")

        while True:
            await asyncio.sleep(0.5)
            final_design = await client.job.design.runs.by_run_id(design_run.run_id).get()
            if final_design.status in TERMINAL:
                break

        print(f"  Design run {final_design.status.value} in {final_design.elapsed_time}")
        if final_design.status != models.AnalysisRunStatus.Completed:
            raise RuntimeError(f"Design run did not complete: {final_design.error_message}")
        print()

        # == Step 10 — What the run did ================================
        print("Design run summary:")
        print(f"  Iterations:       {final_design.iterations}")
        print(f"  Sections updated: {final_design.sections_updated}")
        print(f"  Analysis re-run:  {final_design.analysis_rerun}")
        print(f"  Members checked:  {final_design.members_checked}, failed: {final_design.members_failed}")
        for warning in final_design.warnings or []:
            print(f"  Warning: {warning}")

        # Re-read the member to see which section the design chose.
        designed_member = await client.job.structure.members.by_id(member.id).get()
        designed_section = await client.job.structure.sections.by_id(designed_member.section).get()
        print(f"  Section: {initial_section.name}  ->  {designed_section.name}")
        print()

        # == Step 11 — Check summary for the final section =============
        print("Steel member check summary:")
        summary = await client.job.query.design.steel_member.check_summary.get(
            members=to_filter_string([member.id]),
        )

        for row in summary.results or []:
            print(f"  Member {row.member}: {row.section}")
            print(f"    Load factor:   {row.load_factor:.3f}  (flag: {row.flag})")
            print(f"    Critical case: {row.critical_case}")
            print(f"    Failure mode:  {row.failure}")
        print()

        # == Step 12 — Save and close ==================================
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
