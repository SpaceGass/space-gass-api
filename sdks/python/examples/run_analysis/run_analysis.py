"""
Example: Run a Linear Static Analysis

Demonstrates how to:
  1. Open an existing SPACE GASS project
  2. Start a linear static analysis run
  3. Poll for progress until completion
  4. Display results summary
  5. Query node reactions from the completed analysis

Prerequisites:
  - SPACE GASS API running locally (default: https://localhost:53483)
  - A valid API key
  - An existing .sg project file with structure and loads defined
"""

import asyncio
import os
import sys

from client_factory import create_client
from space_gass_api.models.open_job_request import OpenJobRequest
from space_gass_api.models.static_settings_update import StaticSettingsUpdate
from space_gass_api.models.analysis_run_status import AnalysisRunStatus

# -- Configuration ------------------------------------------------
# Path to an existing SPACE GASS project file with structure and loads.
# Change this to point to your own project file.
project_file_path = os.path.join(
    os.path.expanduser("~/Desktop"),
    "SpaceGass Examples",
    "MyProject.sg",
)

poll_interval_s = 0.5  # How often to poll for progress (seconds)


async def main() -> int:
    client = create_client()

    try:
        # -- Open the project ------------------------------------------
        print(f"Opening project: {project_file_path}")
        await client.job.open.post(
            OpenJobRequest(file_path=project_file_path),
        )
        print("Project opened.")
        print()

        # -- Start a linear static analysis ----------------------------
        # The body uses PATCH semantics — only non-null fields override
        # the current job settings. Pass an empty object to run with
        # current settings as-is.
        print("Starting linear static analysis...")
        run = await client.job.analysis.static.run_linear.post(
            StaticSettingsUpdate(),
        )

        if run is None:
            print("Error: No response from run-linear endpoint.", file=sys.stderr)
            return 1

        print(f"  Run ID:  {run.run_id}")
        print(f"  Status:  {run.status}")
        print()

        # -- Poll for progress until completion ------------------------
        print("Polling for progress...")
        print()

        last_step = -1
        run_id = run.run_id

        while True:
            await asyncio.sleep(poll_interval_s)

            status = await client.job.analysis.runs.by_run_id(str(run_id)).get()
            if status is None:
                break

            # Print progress updates
            if status.progress is not None:
                p = status.progress
                step_info = f"Step {p.current_step}/{p.total_steps}"
                pct_info = f"{p.iteration_percentage}%"
                status_text = p.status_text or ""
                load_case = (
                    f" | Load cases: {p.load_case_status}"
                    if p.load_case_status
                    else ""
                )

                # Print step label when it changes
                if p.current_step != last_step and p.step_labels:
                    step_index = p.current_step or 0
                    if step_index < len(p.step_labels):
                        label = p.step_labels[step_index]
                        if label:
                            print(f"  [{step_info}] {label}")
                    last_step = p.current_step if p.current_step is not None else -1

                line = f"\r  {step_info} | {pct_info}{load_case} | {status_text}"
                print(f"{line:<80}", end="", flush=True)

            elif status.elapsed_time is not None:
                line = f"\r  Status: {status.status} | Elapsed: {status.elapsed_time}"
                print(f"{line:<80}", end="", flush=True)

            # Check for terminal states
            if status.status in (
                AnalysisRunStatus.Completed,
                AnalysisRunStatus.Failed,
                AnalysisRunStatus.Cancelled,
            ):
                print()
                print()

                # -- Display result summary --------------------------------
                print(f"Analysis {status.status}!")
                print(f"  Elapsed time: {status.elapsed_time}")

                if status.header:
                    print(f"  Header: {status.header}")

                # Show parameters
                if status.parameters and status.parameters.additional_data:
                    print("  Parameters:")
                    for key, value in status.parameters.additional_data.items():
                        print(f"    {key} {value}")

                # Show convergence history (non-linear only)
                if status.convergence_history:
                    print("  Convergence history:")
                    for entry in status.convergence_history:
                        print(f"    Iteration {entry.iteration}: {entry.percentage}%")

                # Show warnings
                if status.warnings:
                    print(f"  Warnings ({len(status.warnings)}):")
                    for warning in status.warnings:
                        print(f"    {warning}")

                # Show error
                if status.error_message:
                    print(f"  Error: {status.error_message}", file=sys.stderr)

                break

        # -- Query results (only if completed) -------------------------
        print()
        print("Querying node reactions...")

        query_result = await client.job.query.analysis.static.node.reactions.get()
        reactions = query_result.results if query_result else None
        if reactions:
            print(f"  Found {len(reactions)} reaction result(s).")
            # Print first few reactions as a sample
            for r in reactions[:3]:
                print(
                    f"    Node {r.key}, LC {r.case}: "
                    f"FX={r.fx:.2f}, FY={r.fy:.2f}, FZ={r.fz:.2f}"
                )
            if len(reactions) > 3:
                print(f"    ... and {len(reactions) - 3} more.")
        else:
            print("  No reactions found.")

        # -- Close the project -----------------------------------------
        print()
        print("Closing project...")
        await client.job.close.post()
        print("Project closed.")

    except Exception as ex:
        print(f"Error: {ex}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
