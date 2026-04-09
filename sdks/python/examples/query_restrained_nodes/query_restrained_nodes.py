"""
Example: Query Restrained Nodes and Their Reactions

Demonstrates how to:
  1. Open an existing SPACE GASS project
  2. Filter nodes to only those with restraints
  3. Retrieve reaction results for the restrained nodes
  4. Display the results in a formatted table

Prerequisites:
  - SPACE GASS API running locally (default: http://localhost:5000)
  - A valid API key
  - An existing .sg project file that has been analysed
"""

import asyncio
import sys

from kiota_abstractions.base_request_configuration import RequestConfiguration

from extensions.client_extensions import create_client
from space_gass_api.models.open_job_request import OpenJobRequest
from space_gass_api.models.node_type_filter import NodeTypeFilter
from space_gass_api.job.structure.nodes.nodes_request_builder import NodesRequestBuilder
from space_gass_api.job.query.analysis.static.node.reactions.reactions_request_builder import ReactionsRequestBuilder

# -- Configuration ------------------------------------------------
# Update this path to match your local environment.
PROJECT_FILE_PATH = r"C:\Path\To\Your\Project.sg"


async def main() -> int:
    client = create_client()

    try:
        # -- Open the project ------------------------------------------
        print(f"Opening project: {PROJECT_FILE_PATH}")
        await client.job.open.post(OpenJobRequest(file_path=PROJECT_FILE_PATH))
        print("Project opened successfully.")
        print()

        # -- Get restrained nodes --------------------------------------
        print("Querying restrained nodes...")

        query_params = NodesRequestBuilder.NodesRequestBuilderGetQueryParameters(
            node_type=NodeTypeFilter.Restrained,
        )
        config = RequestConfiguration(query_parameters=query_params)
        restrained_nodes = await client.job.structure.nodes.get(request_configuration=config)

        if not restrained_nodes:
            print("  No restrained nodes found in this project.")
        else:
            print(f"  Found {len(restrained_nodes)} restrained node(s):")
            print()
            print(f"  {'Node':<8} {'X':>12} {'Y':>12} {'Z':>12}")
            print(f"  {'-' * 8} {'-' * 12} {'-' * 12} {'-' * 12}")

            for node in restrained_nodes:
                print(f"  {node.key:<8} {node.x:>12.3f} {node.y:>12.3f} {node.z:>12.3f}")

            # -- Get reactions for restrained nodes --------------------
            print()
            print("Retrieving reactions for restrained nodes...")

            node_keys = [node.key for node in restrained_nodes]

            reaction_params = ReactionsRequestBuilder.ReactionsRequestBuilderGetQueryParameters(
                keys=node_keys,
            )
            reaction_config = RequestConfiguration(query_parameters=reaction_params)
            reaction_result = await client.job.query.analysis.static.node.reactions.get(
                request_configuration=reaction_config,
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
                        f"  {r.key:<8} {r.case:<8} {r.fx:>12.3f} {r.fy:>12.3f} {r.fz:>12.3f}"
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
