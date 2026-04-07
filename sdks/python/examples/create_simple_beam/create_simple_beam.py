"""
Example: Create a Simple Beam Model from Scratch

Demonstrates how to:
  1. Create a new blank SPACE GASS project
  2. Add two nodes
  3. Apply restraints (fixed + pinned)
  4. Create a beam member between the nodes
  5. Save the project to disk

Prerequisites:
  - SPACE GASS API running locally (default: https://localhost:53483)
  - A valid API key
"""

import asyncio
import os
import sys

from extensions.client_extensions import create_client
from space_gass_api.models.save_job_request import SaveJobRequest
from space_gass_api.models.member_create import MemberCreate
from space_gass_api.models.node_create import NodeCreate
from space_gass_api.models.node_restraint_create import NodeRestraintCreate

# -- Configuration ------------------------------------------------
save_file_path = os.path.join(
    os.path.expanduser("~/Desktop"),
    "SpaceGass Examples",
    "SimpleBeam.sg",
)


async def main() -> int:
    client = create_client()

    try:
        # -- Create a new blank project --------------------------------
        print("Creating new blank project...")
        await client.job.new.post()
        print("New project created.")
        print()

        # -- Create two nodes ------------------------------------------
        print("Creating nodes...")

        node1 = await client.job.structure.nodes.post(
            NodeCreate(x=0.0, y=0.0, z=0.0),
        )
        print(f"  Node {node1.key}: ({node1.x}, {node1.y}, {node1.z})")

        node2 = await client.job.structure.nodes.post(
            NodeCreate(x=6.0, y=0.0, z=0.0),
        )
        print(f"  Node {node2.key}: ({node2.x}, {node2.y}, {node2.z})")
        print()

        # -- Apply restraints ------------------------------------------
        # Restraint code: 6 characters for TX, TY, TZ, RX, RY, RZ
        #   F = Free, R = Restrained
        print("Applying restraints...")

        # Node 1: Fixed support (all DOFs restrained)
        await client.job.structure.nodes.by_key(node1.key).restraint.post(
            NodeRestraintCreate(restraint_code="RRRRRR"),
        )
        print(f"  Node {node1.key}: Fixed (RRRRRR)")

        # Node 2: Pinned support (translations restrained, rotations free)
        await client.job.structure.nodes.by_key(node2.key).restraint.post(
            NodeRestraintCreate(restraint_code="RRRFFF"),
        )
        print(f"  Node {node2.key}: Pinned (RRRFFF)")
        print()

        # -- Create a beam member between the two nodes ----------------
        print("Creating beam member...")

        member = await client.job.structure.members.post(
            MemberCreate(node_a=node1.key, node_b=node2.key),
        )
        print(f"  Member {member.key}: Node {member.node_a} -> Node {member.node_b}")
        print()

        # -- Summary ---------------------------------------------------
        print("Simple beam model created successfully!")
        print(f"  Nodes:   {node1.key}, {node2.key}")
        print(f"  Members: {member.key}")
        print(f"  Span:    6.0 (length units)")

        # -- Save the project ------------------------------------------
        # New jobs must use save_as to establish a file path.
        print()
        print(f"Saving project to: {save_file_path}")
        await client.job.save.post(
            SaveJobRequest(file_path=save_file_path),
        )
        print("Project saved.")

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
