"""
Example: Create a Geodesic Dome

Builds a geodesic hemisphere from an icosahedron subdivision, showcasing
the bulk creation endpoints for nodes, members, and restraints.

The dome is parametric — adjust RADIUS and FREQUENCY below to change
the geometry. All 19 CHS sizes are used as sections, assigned by
elevation to produce concentric colour bands.

Prerequisites:
  - SPACE GASS API running locally (default: http://localhost:34560)
  - The "Aust300" section library installed (default in SPACE GASS)
"""

import asyncio
import math
import os
import sys
import time
import winreg

from space_gass_api import SpaceGassApiClient
import space_gass_api.models as models


# -- Parametric Configuration --------------------------------------
# Adjust these values to change the dome geometry and member sizing.

RADIUS = 150.0       # Dome radius in metres
FREQUENCY = 45        # Subdivision frequency (1-50, higher = more triangles)

# All CHS sections from Aust300 — each gets its own colour in SPACE GASS.
# Assigned to members by elevation so the dome shows concentric colour bands.
SECTIONS = [
    "273.1x4.8 CHS",
    "273.1x6.4 CHS",
    "273.1x9.3 CHS",
    "273.1x12.7 CHS",
    "323.9x6.4 CHS",
    "323.9x9.5 CHS",
    "323.9x12.7 CHS",
    "355.6x6.4 CHS",
    "355.6x9.5 CHS",
    "355.6x12.7 CHS",
    "406.4x6.4 CHS",
    "406.4x9.5 CHS",
    "406.4x12.7 CHS",
    "457x6.4 CHS",
    "457x9.5 CHS",
    "457x12.7 CHS",
    "508x6.4 CHS",
    "508x9.5 CHS",
    "508x12.7 CHS",
]

with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders") as _k:
    _DESKTOP = winreg.QueryValueEx(_k, "Desktop")[0]

SAVE_PATH = os.path.join(_DESKTOP, "SpaceGass Examples-py", "GeodesicDome.sg")


# -- Main ----------------------------------------------------------

async def main() -> int:
    if not 1 <= FREQUENCY <= 50:
        print("FREQUENCY must be between 1 and 50.", file=sys.stderr)
        return 1

    # Generate dome geometry.
    print(f"Generating geodesic hemisphere (radius={RADIUS}m, frequency={FREQUENCY})...")
    vertices, edges, base_indices = generate_geodesic_hemisphere(RADIUS, FREQUENCY)
    print(f"  {len(vertices)} nodes, {len(edges)} members, {len(base_indices)} base restraints")
    print()

    t_total = time.perf_counter()

    client = SpaceGassApiClient.create_client("http://localhost:34560")

    try:
        # == Create a new blank project ================================
        print("Creating new blank project...")
        await client.job.new.post()
        print()

        # == Add material ==============================================
        print("Adding steel material...")
        steel = await client.job.structure.materials.library.post(
            models.MaterialLibraryCreate(library="Aust", name="STEEL"))
        print(f"  Material {steel.id}: {steel.name}")
        print()

        # == Add sections (one per CHS size for colour bands) =========
        print(f"Adding {len(SECTIONS)} sections...")
        sections = []
        for name in SECTIONS:
            s = await client.job.structure.sections.library.post(
                models.SectionLibraryCreate(library="Aust300", name=name, mark="CHS"))
            sections.append(s)
        print(f"  {len(sections)} sections added")
        print()

        # == Bulk-create nodes =========================================
        print(f"Creating {len(vertices)} nodes (bulk)...")
        node_creates = [
            models.NodeCreate(x=round(x, 6), y=round(y, 6), z=round(z, 6))
            for x, y, z in vertices
        ]
        t0 = time.perf_counter()
        node_result = await client.job.structure.nodes.bulk.post(node_creates)
        t_nodes = time.perf_counter() - t0

        if node_result.errors:
            print(f"  WARNING: {len(node_result.errors)} node(s) failed", file=sys.stderr)
            for e in node_result.errors[:5]:
                print(f"    {e}", file=sys.stderr)

        created_nodes = node_result.succeeded
        print(f"  {len(created_nodes)} nodes created in {t_nodes:.2f}s")

        # Build a map from local vertex index → API node Id.
        node_id_map: dict[int, int] = {}
        for local_idx, node in enumerate(created_nodes):
            node_id_map[local_idx] = node.id
        print()

        # == Bulk-create members =======================================
        print(f"Creating {len(edges)} members (bulk)...")
        n_sec = len(sections)
        member_creates = []
        for a, b in edges:
            mid_y = (vertices[a][1] + vertices[b][1]) / 2
            band = min(int(mid_y / RADIUS * n_sec), n_sec - 1)
            member_creates.append(models.MemberCreate(
                node_a=node_id_map[a],
                node_b=node_id_map[b],
                section=sections[band].id,
                material=steel.id,
                type="Normal",
            ))
        t0 = time.perf_counter()
        member_result = await client.job.structure.members.bulk.post(member_creates)
        t_members = time.perf_counter() - t0

        if member_result.errors:
            print(f"  WARNING: {len(member_result.errors)} member(s) failed", file=sys.stderr)
            for e in member_result.errors[:5]:
                print(f"    {e}", file=sys.stderr)

        print(f"  {len(member_result.succeeded)} members created in {t_members:.2f}s")
        print()

        # == Bulk-create base restraints ===============================
        print(f"Restraining {len(base_indices)} base nodes (pinned)...")
        restraint_creates = [
            models.NodeRestraintCreate(
                node=node_id_map[idx],
                restraint_code="FFFFFF",
            )
            for idx in sorted(base_indices)
        ]
        t0 = time.perf_counter()
        restraint_result = await client.job.structure.node_restraints.bulk.post(
            restraint_creates)
        t_restraints = time.perf_counter() - t0

        if restraint_result.errors:
            print(f"  WARNING: {len(restraint_result.errors)} restraint(s) failed",
                  file=sys.stderr)

        print(f"  {len(restraint_result.succeeded)} restraints applied in {t_restraints:.2f}s")
        print()

        # == Save ======================================================
        print(f"Saving model to: {SAVE_PATH}")
        await client.job.save.post(
            models.SaveJobRequest(file_path=SAVE_PATH))
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
        try:
            print("Closing project...")
            await client.job.close.post()
            print("Project closed.")
        except Exception as close_ex:
            print(f"Warning: failed to close job: {close_ex}", file=sys.stderr)

    print(f"Total time: {time.perf_counter() - t_total:.2f}s")
    return 0


# -- Geodesic Geometry ---------------------------------------------

def _normalize(x: float, y: float, z: float):
    length = math.sqrt(x * x + y * y + z * z)
    return (x / length, y / length, z / length)


def generate_geodesic_hemisphere(radius: float, frequency: int):
    """
    Generate vertices and edges for a geodesic hemisphere.

    Algorithm:
      1. Build a vertex-up icosahedron (12 vertices, 20 triangular faces)
      2. Subdivide each face into frequency² smaller triangles
      3. Project every vertex onto the sphere surface
      4. Keep the upper hemisphere (y >= 0) and snap the base ring to y = 0
      5. Collect unique edges from the kept triangles

    Returns (vertices, edges, base_indices) where:
      - vertices:     list of (x, y, z) tuples
      - edges:        list of (i, j) index pairs into vertices
      - base_indices: set of vertex indices on the base ring (y = 0)
    """
    # -- Icosahedron (vertex-up orientation) ---------------------------
    # Top and bottom poles on the Y axis; two rings of 5 vertices each.
    top = (0.0, 1.0, 0.0)
    bottom = (0.0, -1.0, 0.0)

    upper_ring = []
    lower_ring = []
    for k in range(5):
        angle_upper = 2 * math.pi * k / 5
        angle_lower = 2 * math.pi * k / 5 + math.pi / 5  # rotated 36°

        r_ring = 2.0 / math.sqrt(5)
        y_ring = 1.0 / math.sqrt(5)

        upper_ring.append(
            _normalize(r_ring * math.cos(angle_upper), y_ring,
                       r_ring * math.sin(angle_upper)))
        lower_ring.append(
            _normalize(r_ring * math.cos(angle_lower), -y_ring,
                       r_ring * math.sin(angle_lower)))

    ico_verts = [top] + upper_ring + lower_ring + [bottom]
    # indices: 0=top, 1-5=upper, 6-10=lower, 11=bottom

    ico_faces = []
    for i in range(5):
        n = (i + 1) % 5
        # Top cap — 5 triangles from top vertex to upper ring
        ico_faces.append((0, 1 + i, 1 + n))
        # Upper band — 5 triangles bridging upper and lower rings
        ico_faces.append((1 + i, 6 + i, 1 + n))
        # Lower band — 5 triangles bridging lower and upper rings
        ico_faces.append((6 + i, 6 + n, 1 + n))
        # Bottom cap — 5 triangles from bottom vertex to lower ring
        ico_faces.append((11, 6 + n, 6 + i))

    # -- Subdivide and project ----------------------------------------
    vertex_map: dict[tuple[float, float, float], int] = {}
    vertex_list: list[tuple[float, float, float]] = []
    edge_set: set[tuple[int, int]] = set()

    def _add_vertex(x: float, y: float, z: float) -> int:
        nx, ny, nz = _normalize(x, y, z)
        key = (round(nx, 10), round(ny, 10), round(nz, 10))
        if key not in vertex_map:
            vertex_map[key] = len(vertex_list)
            vertex_list.append((nx, ny, nz))
        return vertex_map[key]

    def _add_edge(a: int, b: int):
        edge_set.add((min(a, b), max(a, b)))

    for face in ico_faces:
        v0 = ico_verts[face[0]]
        v1 = ico_verts[face[1]]
        v2 = ico_verts[face[2]]

        grid: dict[tuple[int, int], int] = {}
        for i in range(frequency + 1):
            for j in range(frequency + 1 - i):
                wi = i / frequency
                wj = j / frequency
                w0 = 1.0 - wi - wj
                px = w0 * v0[0] + wi * v1[0] + wj * v2[0]
                py = w0 * v0[1] + wi * v1[1] + wj * v2[1]
                pz = w0 * v0[2] + wi * v1[2] + wj * v2[2]
                grid[(i, j)] = _add_vertex(px, py, pz)

        for i in range(frequency):
            for j in range(frequency - i):
                a = grid[(i, j)]
                b = grid[(i + 1, j)]
                c = grid[(i, j + 1)]
                _add_edge(a, b)
                _add_edge(b, c)
                _add_edge(a, c)
                if i + j + 1 < frequency:
                    d = grid[(i + 1, j + 1)]
                    _add_edge(b, d)
                    _add_edge(c, d)

    # -- Hemisphere filter --------------------------------------------
    # Keep vertices with y >= 0 (with tolerance for floating-point).
    # Snap near-zero y values to exactly 0 → these form the base ring.
    tolerance = 0.6 / frequency
    keep: dict[int, int] = {}      # old index → new index
    vertices: list[tuple[float, float, float]] = []
    base_indices: set[int] = set()

    for old_idx, (nx, ny, nz) in enumerate(vertex_list):
        if ny < -tolerance:
            continue
        if ny < tolerance:
            ny = 0.0
        # Scale unit-sphere vertex to target radius.
        # For base vertices (y=0), push them out to the full radius
        # in the XZ plane so the base ring sits on the sphere surface.
        if ny == 0.0:
            r_xz = math.sqrt(nx * nx + nz * nz)
            if r_xz > 1e-12:
                sx = nx / r_xz * radius
                sz = nz / r_xz * radius
            else:
                sx, sz = nx * radius, nz * radius
            vertices.append((sx, 0.0, sz))
            new_idx = len(vertices) - 1
            base_indices.add(new_idx)
        else:
            vertices.append((nx * radius, ny * radius, nz * radius))
            new_idx = len(vertices) - 1
        keep[old_idx] = new_idx

    # Filter edges to kept vertices only.
    edges: list[tuple[int, int]] = []
    for a, b in edge_set:
        if a in keep and b in keep:
            edges.append((keep[a], keep[b]))

    return vertices, edges, base_indices


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
