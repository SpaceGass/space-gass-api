"""
Example: Bridge Grillage with a T44 Moving Load

Python port of the C# Example.GrillageMovingLoad. Builds a 3-span, 2-lane
grillage and runs an AS 5100 T44 moving-load analysis — demonstrating the
moving-load API (vehicle import, travel paths, scenario, generation). The
girder + concrete deck sections and their materials can't be created via the
API yet, so they come from GrillageTemplate.sgbase (shipped next to this
example); everything else is built here.

Prerequisites:
  - SPACE GASS API running locally (default http://localhost:34560)
  - The "Australia" vehicle library installed (for T44)
  - GrillageTemplate.sgbase in this folder (uploaded via new-from-template)
"""

import asyncio
import os
import sys
import winreg

from space_gass_api import NewFromTemplateRequest, SpaceGassApiClient
import space_gass_api.models as models
from space_gass_api.utils import to_filter_string

# -- Configuration ------------------------------------------------
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "GrillageTemplate.sgbase")

with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders") as _k:
    _DESKTOP = winreg.QueryValueEx(_k, "Desktop")[0]

SAVE_FILE_PATH = os.path.join(_DESKTOP, "SpaceGass Examples-py", "GrillageMovingLoad.sg")

# Section + material Ids defined in the template.
GIRDER_SECTION_ID = 1          # Bridge Girder (steel WB)
INTERIOR_STRIP_SECTION_ID = 2  # 1.0 m concrete deck strip
END_STRIP_SECTION_ID = 3       # 0.5 m concrete deck strip (end lines)
STEEL_MATERIAL_ID = 1
CONCRETE_MATERIAL_ID = 2

# Geometry. X = along the bridge, Z = across, Y = up.
SPAN_LENGTHS = [20.0, 20.0, 20.0]          # 3 spans, 60 m total
GIRDER_Z = [0.0, 1.75, 3.5, 5.25, 7.0]     # 5 girders, 1.75 m c/c
STRIP_SPACING = 1.0                        # transverse strips @ 1 m
LANE_PATH_GIRDER_INDICES = [1, 3]          # girders 2 & 4 = lane centrelines
WEARING_SURFACE_PRESSURE = 2.0             # SDL, kN/m^2

NUM_GIRDERS = len(GIRDER_Z)
TOTAL_LENGTH = sum(SPAN_LENGTHS)
NUM_STATIONS = round(TOTAL_LENGTH / STRIP_SPACING) + 1
NUM_BAYS = NUM_GIRDERS - 1

# Stations that sit on a support (abutment / pier) line.
_support_xs = [0.0]
for _span in SPAN_LENGTHS:
    _support_xs.append(_support_xs[-1] + _span)
SUPPORT_STATIONS = sorted({round(x / STRIP_SPACING) for x in _support_xs})

TOTAL_MEMBERS = NUM_GIRDERS * (NUM_STATIONS - 1) + NUM_STATIONS * NUM_BAYS


# Deterministic Ids so the grid wires up without round-tripping.
def station_x(i: int) -> float:
    return i * STRIP_SPACING


def node_id(g: int, i: int) -> int:
    return g * NUM_STATIONS + i + 1


def girder_member_id(g: int, i: int) -> int:
    return g * (NUM_STATIONS - 1) + i + 1


def strip_member_id(i: int, b: int) -> int:
    return NUM_GIRDERS * (NUM_STATIONS - 1) + i * NUM_BAYS + b + 1


async def main() -> int:
    client = SpaceGassApiClient.create_client("http://localhost:34560")

    try:
        # New job from the template (fresh, unsaved — template file is untouched).
        if not os.path.isfile(TEMPLATE_PATH):
            raise FileNotFoundError(f"Template not found: {TEMPLATE_PATH}")

        print(f"Uploading template: {os.path.basename(TEMPLATE_PATH)}")
        await client.job.new_from_template.post(NewFromTemplateRequest(TEMPLATE_PATH))
        print("New job created from template (unsaved).")
        print()

        # Show what the template provides, then validate the Ids we rely on.
        sections = await client.job.structure.sections.get() or []
        materials = await client.job.structure.materials.get() or []
        primary_cases = await client.job.loads.load_cases.get() or []

        print("Template sections:")
        for s in sections:
            print(f"  [{s.id}] {s.name}  (mark: {s.mark}, A={s.a}, Iz={s.iz})")
        print("Template materials:")
        for m in materials:
            print(f"  [{m.id}] {m.name}  (E={m.youngs_modulus})")
        print("Template primary load cases:")
        for lc in primary_cases:
            print(f"  [{lc.id}] {lc.title}")
        print()

        section_ids = {s.id for s in sections}
        for sid, what in [
            (GIRDER_SECTION_ID, "girder section"),
            (INTERIOR_STRIP_SECTION_ID, "1 m deck-strip section"),
            (END_STRIP_SECTION_ID, "0.5 m deck-strip section"),
        ]:
            if sid not in section_ids:
                raise RuntimeError(
                    f"Template is missing the expected {what} (Id {sid}). "
                    f"Sections found: {sorted(section_ids)}.")
        material_ids = {m.id for m in materials}
        for mid, what in [(STEEL_MATERIAL_ID, "STEEL"), (CONCRETE_MATERIAL_ID, "Concrete")]:
            if mid not in material_ids:
                raise RuntimeError(
                    f"Template is missing the expected {what} material (Id {mid}).")
        if not primary_cases:
            raise RuntimeError("The template defines no load cases — expected a self-weight case.")

        self_weight_case = primary_cases[0]   # pre-baked self-weight case
        print(f"Using self-weight case [{self_weight_case.id}] '{self_weight_case.title}'.")
        print()

        # Nodes — a grid of girders x stations.
        print(f"Creating {NUM_GIRDERS * NUM_STATIONS} nodes "
              f"({NUM_GIRDERS} girders x {NUM_STATIONS} stations)...")
        nodes = [
            models.NodeCreate(id=node_id(g, i), x=station_x(i), y=0.0, z=GIRDER_Z[g])
            for g in range(NUM_GIRDERS)
            for i in range(NUM_STATIONS)
        ]
        node_result = await client.job.structure.nodes.bulk.post(nodes)
        if node_result and node_result.errors:
            raise RuntimeError(
                f"Node bulk create reported {len(node_result.errors)} error(s); "
                f"first: {node_result.errors[0].error}")
        print(f"  {len(nodes)} nodes created.")
        print()

        # Members — longitudinal girders, plus transverse deck strips (the end
        # lines use the 0.5 m strip, interior lines the 1 m strip).
        print(f"Creating {TOTAL_MEMBERS} members (girders + deck strips)...")
        members = [
            models.MemberCreate(
                id=girder_member_id(g, i),
                node_a=node_id(g, i),
                node_b=node_id(g, i + 1),
                section=GIRDER_SECTION_ID,
                material=STEEL_MATERIAL_ID,
            )
            for g in range(NUM_GIRDERS)
            for i in range(NUM_STATIONS - 1)
        ]
        for i in range(NUM_STATIONS):
            is_end_line = i == 0 or i == NUM_STATIONS - 1
            for b in range(NUM_BAYS):
                members.append(models.MemberCreate(
                    id=strip_member_id(i, b),
                    node_a=node_id(b, i),
                    node_b=node_id(b + 1, i),
                    section=END_STRIP_SECTION_ID if is_end_line else INTERIOR_STRIP_SECTION_ID,
                    material=CONCRETE_MATERIAL_ID,
                ))

        member_result = await client.job.structure.members.bulk.post(members)
        if member_result and member_result.errors:
            raise RuntimeError(
                f"Member bulk create reported {len(member_result.errors)} error(s); "
                f"first: {member_result.errors[0].error}")
        print(f"  {len(members)} members created.")
        print()

        # Bearings. Restraint code is TX TY TZ RX RY RZ (F = fixed, R = released):
        # abutment 1 is fixed; the piers and abutment 2 are guided longitudinally.
        print("Restraining bearing lines...")
        support_node_ids: list[int] = []
        for idx, station in enumerate(SUPPORT_STATIONS):
            code = "FFFRRR" if idx == 0 else "RFFRRR"
            for g in range(NUM_GIRDERS):
                nid = node_id(g, station)
                await client.job.structure.node_restraints.post(
                    models.NodeRestraintCreate(node=nid, restraint_code=code))
                support_node_ids.append(nid)
        print(f"  {len(support_node_ids)} support nodes restrained.")
        print()

        # Superimposed dead load (wearing surface) as a UDL on each deck strip;
        # the end strips carry half the longitudinal tributary width.
        print(f"Applying {WEARING_SURFACE_PRESSURE} kN/m^2 SDL to the deck strips...")
        sdl_case = await client.job.loads.load_cases.post(
            models.LoadCaseCreate(id=2, title="G2 - Superimposed Dead Load (wearing surface)"))

        sdl_loads = []
        for i in range(NUM_STATIONS):
            tributary_x = STRIP_SPACING / 2.0 if (i == 0 or i == NUM_STATIONS - 1) else STRIP_SPACING
            udl = -WEARING_SURFACE_PRESSURE * tributary_x   # kN/m, downward
            for b in range(NUM_BAYS):
                sdl_loads.append(models.MemberDistributedLoadCreate(
                    load_case=sdl_case.id,
                    member=strip_member_id(i, b),
                    position_units=models.LoadPositionUnits.Percent,
                    start_position=0.0,
                    finish_position=100.0,
                    fy_start=udl,
                    fy_finish=udl,
                ))
        await client.job.loads.member_distributed_loads.bulk.post(sdl_loads)
        print(f"  SDL applied to {len(sdl_loads)} deck strips (case {sdl_case.id}).")
        print()

        # Total dead load = self-weight + SDL. A scenario can combine with only
        # one load case, so roll the permanent loads into a single combination.
        total_dead_load = await client.job.loads.combination_load_cases.post(
            models.CombinationLoadCaseCreate(
                id=50,
                title="Total Dead Load (self-weight + SDL)",
                combination_items=[
                    models.CombinationLoadCaseItem(load_case=self_weight_case.id, multiplying_factor=1.0),
                    models.CombinationLoadCaseItem(load_case=sdl_case.id,         multiplying_factor=1.0),
                ],
            ))
        print(f"Total Dead Load combination = case {total_dead_load.id}.")
        print()

        # --- T44 moving load ---
        print("Setting up the T44 moving load...")

        await client.job.loads.moving_loads.settings.patch(
            models.MovingLoadSettingsUpdate(
                apply_to_closest_member=True,
                check_vertical_proximity=False,
                keep_loads_within_travel_path=False,
            ))

        # Import T44 from the vehicle library and print its wheel layout.
        t44 = await client.job.loads.moving_loads.vehicles.library.post(
            models.MovingLoadVehicleLibraryCreate(name="T44-3", library="Australia"))
        print(f"  Imported vehicle [{t44.id}] {t44.name} from {t44.library}.")

        wheels = t44.loads or []
        load_units = t44.load_units
        if not wheels:
            full = await client.job.loads.moving_loads.vehicles.by_id(t44.id).get()
            wheels = (full.loads if full else None) or wheels
            load_units = (full.load_units if full else None) or load_units

        if not wheels:
            print("  (vehicle returned no wheel loads — check the library item name).")
        else:
            length_unit = load_units.length if load_units else None
            force_unit = load_units.force if load_units else None
            print(f"  T44 wheel loads — {len(wheels)} wheels "
                  f"(units: length={length_unit}, force={force_unit}):")
            print("        #         X         Y        Fx        Fy        Fz")
            for w, wheel in enumerate(wheels, start=1):
                print(f"      {w:>3}  {wheel.x or 0:>8.3f}  {wheel.y or 0:>8.3f}  "
                      f"{wheel.fx or 0:>8.2f}  {wheel.fy or 0:>8.2f}  {wheel.fz or 0:>8.2f}")

            # Truck footprint: longitudinal axle base and transverse wheel track.
            xs = [wheel.x or 0 for wheel in wheels]
            ys = [wheel.y or 0 for wheel in wheels]
            sum_fy = sum(wheel.fy or 0 for wheel in wheels)
            sum_fz = sum(wheel.fz or 0 for wheel in wheels)
            print(f"      Footprint: axle base (X)={max(xs) - min(xs):.3f}, "
                  f"track width (Y)={max(ys) - min(ys):.3f} {length_unit}; "
                  f"total Fy={sum_fy:.1f}, Fz={sum_fz:.1f} {force_unit}")

        # One travel path per lane, centred on girders 2 and 4 (node_key = 0
        # means the x/y/z are absolute coordinates).
        travel_path_ids: list[int] = []
        for k, gi in enumerate(LANE_PATH_GIRDER_INDICES):
            lane_z = GIRDER_Z[gi]
            path = await client.job.loads.moving_loads.travel_paths.post(
                models.MovingLoadTravelPathCreate(name=f"Lane {k + 1} (girder {gi + 1})"))

            await client.job.loads.moving_loads.travel_paths.by_id(path.id).stations.put([
                models.MovingLoadStation(node_key=0, x=0.0,          y=0.0, z=lane_z, radius=0.0),
                models.MovingLoadStation(node_key=0, x=TOTAL_LENGTH, y=0.0, z=lane_z, radius=0.0),
            ])
            travel_path_ids.append(path.id)
            print(f"  Travel path [{path.id}] '{path.name}' along Z = {lane_z} m.")

        # Scenario: a T44 on each lane, combined with the Total Dead Load
        # (1.2 G + 1.5 live, 1.3 dynamic load allowance).
        scenario = await client.job.loads.moving_loads.scenarios.post(
            models.MovingLoadScenarioCreate(
                name="T44 - both lanes",
                include=True,
                starting_load_case=101,
                time_interval=0.5,
                loads=[
                    models.MovingLoadScenarioLoad(
                        load_type=models.MovingLoadType.Vehicle,
                        vehicle_id=t44.id,
                        travel_path_id=travel_path_ids[0],
                        speed=10.0,
                        start_position=0.0,
                        load_factor=1.0,
                        lane_factor=1.0,      # AS 5100 lane modification factor
                        dynamic_factor=1.3,   # T44 dynamic load allowance (~0.3)
                        generate_stationary_lc=models.MovingLoadStationaryOption.StartingLoadCase,
                    ),
                    models.MovingLoadScenarioLoad(
                        load_type=models.MovingLoadType.Vehicle,
                        vehicle_id=t44.id,
                        travel_path_id=travel_path_ids[1],
                        speed=10.0,
                        start_position=0.0,
                        load_factor=1.0,
                        lane_factor=1.0,
                        dynamic_factor=1.3,
                        generate_stationary_lc=models.MovingLoadStationaryOption.StartingLoadCase,
                    ),
                ],
                combinations=[
                    models.MovingLoadCombination(
                        scenario_factor=1.5,
                        combine_with_load_case=total_dead_load.id,
                        load_case_factor=1.2,
                        starting_combination_case=201,
                    ),
                ],
            ))
        print(f"  Scenario [{scenario.id}] '{scenario.name}' created.")

        # Select the elements the loads apply to (the whole grillage). This MUST
        # come after the scenario block — the vehicle/path/scenario setup resets
        # the selection, so an earlier call is silently cleared by generation time.
        elements = await client.job.loads.moving_loads.elements_to_load.patch(
            models.MovingLoadElementsToLoadUpdate(
                members=to_filter_string(list(range(1, TOTAL_MEMBERS + 1)))))
        print(f"  Elements to load: members='{elements.members if elements else None}'.")

        generation = await client.job.loads.moving_loads.generate.post(
            models.MovingLoadGenerateRequest())
        moving_case_ids = [i for i in (generation.generated_load_case_ids or []) if i is not None]
        print(f"  Generated {len(moving_case_ids)} moving load case(s).")
        print()

        # A named filter per member type (selectable in the SPACE GASS UI).
        print("Creating selection filters...")
        await client.job.filters.post(models.FilterCreate(
            name="Girders (WB)",
            sections=models.FilterSectionsUpdate(
                is_active=True, mode=models.FilterMode.Include,
                sections=str(GIRDER_SECTION_ID)),
        ))
        await client.job.filters.post(models.FilterCreate(
            name="Deck slab strips",
            sections=models.FilterSectionsUpdate(
                is_active=True, mode=models.FilterMode.Include,
                sections=f"{INTERIOR_STRIP_SECTION_ID},{END_STRIP_SECTION_ID}"),
        ))
        await client.job.filters.post(models.FilterCreate(
            name="Bridge supports",
            nodes=models.FilterNodesUpdate(
                is_active=True, mode=models.FilterMode.Include,
                nodes=to_filter_string(support_node_ids)),
        ))
        print("  Filters: 'Girders (WB)', 'Deck slab strips', 'Bridge supports'.")
        print()

        print(f"Saving model to: {SAVE_FILE_PATH}")
        await client.job.save.post(models.SaveJobRequest(file_path=SAVE_FILE_PATH))
        print()

        # Analyse, then report the peak girder moment from the T44 envelope.
        run = await client.job.analysis.static.run_linear.post(models.StaticSettingsUpdate())
        print(f"Run {run.run_id} queued; waiting for completion...")

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
            raise RuntimeError(f"Analysis did not complete: {final_run.error_message}")
        print()

        if not moving_case_ids:
            print("No moving load cases were generated — skipping the result query.")
        else:
            # Worst bending moment on the central girder across the moving snapshots.
            centre_girder = NUM_GIRDERS // 2
            centre_members = [girder_member_id(centre_girder, i) for i in range(NUM_STATIONS - 1)]

            forces = await client.job.query.analysis.static.member_intermediate_forces.get(
                load_cases=to_filter_string(moving_case_ids),
                members=to_filter_string(centre_members),
            )

            peak_mz = 0.0
            peak_case = peak_member = None
            for row in (forces.results or []):
                for mz in (row.mz or []):
                    v = abs(mz or 0.0)
                    if v > peak_mz:
                        peak_mz, peak_case, peak_member = v, row.load_case, row.member

            print(f"Peak |Mz| on central girder (line {centre_girder + 1}): {peak_mz:.1f} kNm "
                  f"(member {peak_member}, moving load case {peak_case}).")
        print()

        print(f"Saving analysed model to: {SAVE_FILE_PATH}")
        await client.job.save.post(models.SaveJobRequest(file_path=SAVE_FILE_PATH))
        print("Done.")

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
