"""
Example: Steel Member Design CHECK to AS 4100

Builds the same simply-supported beam as create_simple_beam, analyses
it, then verifies the beam's section against AS 4100:
   1.  Create the client and a new project
   2.  Build the beam (nodes, restraints, material, section, member)
   3.  Load cases, loads and a ULS combination
   4.  Run a linear static analysis and wait for completion
   5.  List the design codes this seat can check to
   6.  Create a steel member design group for the beam
   7.  Configure the general design settings (which groups / cases)
   8.  Configure the AS 4100 code-specific settings
   9.  Start a design CHECK run and poll until it finishes
   10. Query the per-member check summary (load factor, critical case)
   11. Save and close

A CHECK run verifies the members' current sections without changing
the model. See steel_design_optimise for a DESIGN run that selects
new sections.

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

save_file_path = os.path.join(_DESKTOP, "SpaceGass Examples-py", "SteelDesignCheck.sg")

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

        # == Step 2 — Build the beam ===================================
        print("Building a 6 m simply-supported beam...")

        node1 = await client.job.structure.nodes.post(models.NodeCreate(x=0.0, y=0.0, z=0.0))
        node2 = await client.job.structure.nodes.post(models.NodeCreate(x=6.0, y=0.0, z=0.0))

        await client.job.structure.node_restraints.post(
            models.NodeRestraintCreate(node=node1.id, restraint_code="FFFFFF"))
        await client.job.structure.node_restraints.post(
            models.NodeRestraintCreate(node=node2.id, restraint_code="FFFRRR"))

        steel = await client.job.structure.materials.library.post(
            models.MaterialLibraryCreate(library="Aust", name="STEEL"))

        section = await client.job.structure.sections.library.post(
            models.SectionLibraryCreate(library="Aust300", name="360 UB 44.7", mark="B1"))

        member = await client.job.structure.members.post(
            models.MemberCreate(
                node_a=node1.id,
                node_b=node2.id,
                section=section.id,
                material=steel.id,
            ))
        print(f"  Member {member.id}: {section.name} ({steel.name})")
        print()

        # == Step 3 — Load cases, loads and a ULS combination ==========
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

        # == Step 4 — Run a linear static analysis =====================
        # A design run needs static analysis results for the design load
        # cases, so analyse first.
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

        # == Step 5 — List the available design codes ==================
        # Does not need an open job. Each entry says whether this seat is
        # licensed for the code and which edition a run is completed under.
        print("Steel member design codes:")
        codes = await client.job.design.steel_design.codes.get()
        for c in codes:
            print(f"  {str(c.code):8} {c.edition:16} licensed: {c.is_licensed}")

        as4100 = next((c for c in codes if c.code == models.SteelDesignCode.As4100), None)
        if not as4100 or not as4100.is_licensed:
            raise RuntimeError("This seat is not licensed for AS 4100 steel member design.")
        print()

        # == Step 6 — Create a steel member design group ===============
        # A design group (SPACE GASS "Design - Steel Members") spans one or
        # more analytical members. members is a plain comma-separated list
        # of member Ids (ranges are not supported here).
        print("Creating steel member design group...")
        group = await client.job.design.steel_members.post(
            models.SteelMemberCreate(
                id=1,
                description="Floor beam B1",
                members=str(member.id),
                member_type=models.SteelMemberType.Beam,
                strength_grade=models.SteelStrengthGrade.Normal,
                load_height_position=models.LoadHeightPosition.Top,
                # Compression effective lengths: by default these come from a
                # buckling analysis, which this model hasn't run. Give them
                # explicitly as actual lengths (the full 6 m span, pinned ends).
                length_unit_basis=models.LengthUnitBasis.Actual,
                calculate_lc_major_from_buckling=False,
                lc_major=6.0,
                calculate_lc_minor_from_buckling=False,
                lc_minor=6.0,
                # Work out the lateral-torsional buckling length from the
                # flange restraints (the ends are restrained by default).
                calculate_lb_from_flange_restraints=True,
            ))
        print(f"  Design group {group.id}: members {group.members}")
        print()

        # == Step 7 — General design settings ==========================
        # Code-independent settings shared by every design code: which
        # groups and load cases to design/check, section availability, etc.
        # Settings are saved with the job.
        print("Configuring general design settings...")
        settings = await client.job.design.steel_design.settings.patch(
            models.SteelMemberDesignGeneralSettingsUpdate(
                groups=to_filter_string([group.id]),
                load_cases=to_filter_string([uls_case.id]),
                stations=10,            # intermediate stations checked along each member
                load_factor_limit=1.0,
            ))
        print(f"  Groups: {settings.groups}, Load cases: {settings.load_cases}, Stations: {settings.stations}")
        print()

        # == Step 8 — AS 4100 code-specific settings ===================
        # Each design code has its own settings object (AS 4100 and NZS 3404
        # differ). They can be PATCHed at steel-design/{code}/settings, or —
        # as here — passed as a per-run override on the run request; either
        # way they are stored with the job. The steel_design helpers take
        # the code's own settings object and fill in the code discriminator.
        print("Preparing AS 4100 settings...")
        as4100_settings = models.SteelMemberDesignSettingsAS4100Update(
            slenderness_ratio_check=True,
            use_kt_factor_for_tension=True,
        )
        print("  Slenderness ratio check on, Kt factor for tension on")
        print()

        # == Step 9 — Start the CHECK run and poll =====================
        # The body is optional; settings supplied here are written to the
        # job's stored settings before the run starts. Analysis and design
        # runs share one queue, so queue_position may be > 1.
        print(f"Starting {DESIGN_CODE} design CHECK run...")
        design_run = await client.job.design.steel_design.by_code(DESIGN_CODE).run_check.post(
            steel_design.run_check_request(code_settings=as4100_settings))
        print(f"  Run {design_run.run_id} {design_run.status.value}; waiting for completion...")

        while True:
            await asyncio.sleep(0.5)
            final_design = await client.job.design.runs.by_run_id(design_run.run_id).get()
            if final_design.status in TERMINAL:
                break

        print(f"  Design run {final_design.status.value} in {final_design.elapsed_time}")
        if final_design.status != models.AnalysisRunStatus.Completed:
            raise RuntimeError(f"Design run did not complete: {final_design.error_message}")

        # Once Completed the run carries its result summary.
        print(f"  Mode: {final_design.mode.value}, code: {final_design.code.value}")
        print(f"  Members checked: {final_design.members_checked}, failed: {final_design.members_failed}")
        for warning in final_design.warnings or []:
            print(f"  Warning: {warning}")
        print()

        # == Step 10 — Query the check summary =========================
        # One row per member. load_factor is the capacity ratio the member
        # achieved; flag and failure describe the governing check, and
        # critical_case is the load case that governed.
        print("Steel member check summary:")
        summary = await client.job.query.design.steel_member.check_summary.get(
            members=to_filter_string([member.id]),
        )

        for row in summary.results or []:
            print(f"  Member {row.member}: {row.section}")
            print(f"    Load factor:   {row.load_factor:.3f}  (flag: {row.flag})")
            print(f"    Critical case: {row.critical_case}")
            print(f"    Failure mode:  {row.failure}")
            print(f"    Yield stress:  {row.yield_}  Segment length: {row.segment_length}")
        print()

        # == Step 11 — Save and close ==================================
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
