"""
Example: Query Restrained Nodes and Their Reactions

Demonstrates how to:
  1. Open an existing SPACE GASS project
  2. Filter nodes to only those with restraints
  3. Retrieve reaction results for the restrained nodes
  4. Display the results in a formatted table

Prerequisites:
  - SPACE GASS API running locally (default: http://localhost:34560)
  - An existing .sg project file that has been analysed
"""

import asyncio
import sys

from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models
from space_gass_api.utils import to_filter_string

# -- Configuration ------------------------------------------------
# Update this path to match your local environment.
PROJECT_FILE_PATH = r"C:\Path\To\Your\Project.sg"


async def main() -> int:
    client = SpaceGassApiClient.create_client("http://localhost:34560")

    try:
        # -- Open the project ------------------------------------------
        print(f"Opening project: {PROJECT_FILE_PATH}")
        await client.job.open.post(models.OpenJobRequest(file_path=PROJECT_FILE_PATH))
        print("Project opened successfully.")
        print()

        # -- Get restrained nodes --------------------------------------
        print("Querying restrained nodes...")

        restrained_nodes = await client.job.structure.nodes.get(
            node_type=models.NodeTypeFilter.Restrained,
        )

        if not restrained_nodes:
            print("  No restrained nodes found in this project.")
        else:
            print(f"  Found {len(restrained_nodes)} restrained node(s):")
            print()
            print(f"  {'Node':<8} {'X':>12} {'Y':>12} {'Z':>12}")
            print(f"  {'-' * 8} {'-' * 12} {'-' * 12} {'-' * 12}")

            for node in restrained_nodes:
                print(f"  {node.id:<8} {node.x:>12.3f} {node.y:>12.3f} {node.z:>12.3f}")

            # -- Get reactions for restrained nodes --------------------
            print()
            print("Retrieving reactions for restrained nodes...")

            node_filter = to_filter_string(n.id for n in restrained_nodes if n.id is not None)

            reaction_result = await client.job.query.analysis.static.node_reactions.get(
                nodes=node_filter,
            )

            reactions = reaction_result.results if reaction_result else None

            if not reactions:
                print("  No reaction results found. Has the model been analysed?")
            else:
                print(f"  Found {len(reactions)} reaction result(s):")
                print()
                print(
                    f"  {'Node':<8} {'Case':<8} {'Fx':>12} {'Fy':>12} {'Fz':>12}"
                    f" {'Mx':>12} {'My':>12} {'Mz':>12}"
                )
                print(
                    f"  {'-' * 8} {'-' * 8} {'-' * 12} {'-' * 12} {'-' * 12}"
                    f" {'-' * 12} {'-' * 12} {'-' * 12}"
                )

                for r in reactions:
                    print(
                        f"  {r.node:<8} {r.load_case:<8} {r.fx:>12.3f} {r.fy:>12.3f} {r.fz:>12.3f}"
                        f" {r.mx:>12.3f} {r.my:>12.3f} {r.mz:>12.3f}"
                    )

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
