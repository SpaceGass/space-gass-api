"""
Example: Quick Start

The end-to-end snippet from the docs Quick Start guide as a runnable
script. Opens a built-in SPACE GASS sample, lists every node, then
closes the job. No project file of your own required.

Prerequisites:
  - SPACE GASS API service running locally (default
    http://localhost:34560/api/v1).
  - The "Portal Frame.SG" sample is shipped with every install,
    but you can list available samples via GET /file/samples or
    in Swagger.
"""

import asyncio
import sys

from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models


async def main() -> int:
    client = SpaceGassApiClient.create_client("http://localhost:34560")

    try:
        print("Opening sample 'Portal Frame.SG'...")
        await client.job.open_sample.post(
            models.OpenSampleRequest(file_name="Portal Frame.SG"),
        )

        nodes = await client.job.structure.nodes.get()
        print(f"Found {len(nodes)} node(s):")
        for node in nodes:
            print(f"  Node {node.id}: ({node.x}, {node.y}, {node.z})")

    except models.ProblemDetails as pd:
        print(f"API error {pd.status}: {pd.title}", file=sys.stderr)
        if pd.detail:
            print(f"  {pd.detail}", file=sys.stderr)
        return 1
    finally:
        print("Closing project...")
        await client.job.close.post()

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
