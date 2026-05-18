using SpaceGassApi;
using SpaceGassApi.Models;


// ---------------------------------------------------------------
// Example: Create a Geodesic Dome
//
// Builds a geodesic hemisphere from an icosahedron subdivision,
// showcasing the bulk creation endpoints for nodes, members,
// and restraints.
//
// The dome is parametric — adjust Radius and Frequency below
// to change the geometry. All 19 CHS sizes are used as sections,
// assigned by elevation to produce concentric colour bands.
//
// Prerequisites:
//   - SPACE GASS API running locally (default: http://localhost:34560)
//   - The "Aust300" section library installed (default in SPACE GASS)
// ---------------------------------------------------------------

// -- Parametric Configuration --------------------------------------
// Adjust these values to change the dome geometry and member sizing.

const double Radius = 150.0;             // Dome radius in metres
const int Frequency = 45;                // Subdivision frequency (1-50, higher = more triangles)
// All CHS sections from Aust300 — each gets its own colour in SPACE GASS.
// Assigned to members by elevation so the dome shows concentric colour bands.
string[] sectionNames =
[
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
];

var saveFilePath = Path.Combine(
    Environment.GetFolderPath(Environment.SpecialFolder.Desktop),
    "SpaceGass Examples",
    "GeodesicDome.sg");


// -- Validate inputs -----------------------------------------------

if (Frequency < 1 || Frequency > 50)
{
    Console.Error.WriteLine("Frequency must be between 1 and 36.");
    return 1;
}


var stopwatch = System.Diagnostics.Stopwatch.StartNew();

// -- Generate dome geometry ----------------------------------------

Console.WriteLine($"Generating geodesic hemisphere (radius={Radius}m, frequency={Frequency})...");

var (vertices, edges, baseIndices) = GenerateGeodesicHemisphere(Radius, Frequency);

Console.WriteLine($"  {vertices.Count} nodes, {edges.Count} members, {baseIndices.Count} base restraints");
Console.WriteLine();


// -- Build the model via the API -----------------------------------

var client = SpaceGassApiClient.CreateClient("http://localhost:34560");

try
{
    // == Create a new blank project ================================
    Console.WriteLine("Creating new blank project...");
    await client.Job.New.PostAsync();
    Console.WriteLine();

    // == Add material ==============================================
    Console.WriteLine("Adding steel material...");
    var steel = await client.Job.Structure.Materials.Library.PostAsync(
        new MaterialLibraryCreate { Library = "Aust", Name = "STEEL" });
    Console.WriteLine($"  Material {steel!.Id}: {steel.Name}");
    Console.WriteLine();

    // == Add sections (one per CHS size for colour bands) =========
    Console.WriteLine($"Adding {sectionNames.Length} sections...");
    var sections = new List<Section>();
    foreach (var name in sectionNames)
    {
        var s = await client.Job.Structure.Sections.Library.PostAsync(
            new SectionLibraryCreate { Library = "Aust300", Name = name, Mark = "CHS" });
        sections.Add(s!);
    }
    Console.WriteLine($"  {sections.Count} sections added");
    Console.WriteLine();

    // == Bulk-create nodes =========================================
    Console.WriteLine($"Creating {vertices.Count} nodes (bulk)...");

    var nodeCreates = vertices.Select(v =>
        new NodeCreate
        {
            X = Math.Round(v.X, 6),
            Y = Math.Round(v.Y, 6),
            Z = Math.Round(v.Z, 6),
        }).ToList();

    var nodeTimer = System.Diagnostics.Stopwatch.StartNew();
    var nodeResult = await client.Job.Structure.Nodes.Bulk.PostAsync(nodeCreates);
    nodeTimer.Stop();

    if (nodeResult!.Errors is { Count: > 0 } nodeErrors)
    {
        Console.Error.WriteLine($"  WARNING: {nodeErrors.Count} node(s) failed");
    }

    var createdNodes = nodeResult.Succeeded!;
    Console.WriteLine($"  {createdNodes.Count} nodes created in {nodeTimer.Elapsed.TotalSeconds:F2}s");

    // Build a map from local vertex index → API node Id.
    var nodeIdMap = new Dictionary<int, int>();
    for (var i = 0; i < createdNodes.Count; i++)
    {
        nodeIdMap[i] = createdNodes[i].Id!.Value;
    }
    Console.WriteLine();

    // == Bulk-create members =======================================
    Console.WriteLine($"Creating {edges.Count} members (bulk)...");

    var nSec = sections.Count;
    var memberCreates = edges.Select(e =>
    {
        var midY = (vertices[e.A].Y + vertices[e.B].Y) / 2;
        var band = Math.Min((int)(midY / Radius * nSec), nSec - 1);
        return new MemberCreate
        {
            NodeA = nodeIdMap[e.A],
            NodeB = nodeIdMap[e.B],
            Section = sections[band].Id,
            Material = steel.Id,
        };
    }).ToList();

    var memberTimer = System.Diagnostics.Stopwatch.StartNew();
    var memberResult = await client.Job.Structure.Members.Bulk.PostAsync(memberCreates);
    memberTimer.Stop();

    if (memberResult!.Errors is { Count: > 0 } memberErrors)
    {
        Console.Error.WriteLine($"  WARNING: {memberErrors.Count} member(s) failed");
    }

    Console.WriteLine($"  {memberResult.Succeeded!.Count} members created in {memberTimer.Elapsed.TotalSeconds:F2}s");
    Console.WriteLine();

    // == Bulk-create base restraints ===============================
    Console.WriteLine($"Restraining {baseIndices.Count} base nodes (fixed)...");

    var restraintCreates = baseIndices
        .OrderBy(idx => idx)
        .Select(idx => new NodeRestraintCreate
        {
            Node = nodeIdMap[idx],
            RestraintCode = "FFFFFF",
        }).ToList();

    var restraintTimer = System.Diagnostics.Stopwatch.StartNew();
    var restraintResult = await client.Job.Structure.NodeRestraints.Bulk.PostAsync(
        restraintCreates);
    restraintTimer.Stop();

    if (restraintResult!.Errors is { Count: > 0 } restraintErrors)
    {
        Console.Error.WriteLine($"  WARNING: {restraintErrors.Count} restraint(s) failed");
    }

    Console.WriteLine($"  {restraintResult.Succeeded!.Count} restraints applied in {restraintTimer.Elapsed.TotalSeconds:F2}s");
    Console.WriteLine();

    // == Save ======================================================
    Console.WriteLine($"Saving model to: {saveFilePath}");
    await client.Job.Save.PostAsync(
        new SaveJobRequest { FilePath = saveFilePath });
    Console.WriteLine("Project saved.");
}
catch (ErrorResponse err)
{
    Console.Error.WriteLine($"API error {err.Status}: {err.Title}");
    if (err.Detail != null)
        Console.Error.WriteLine($"  {err.Detail}");
    if (err.ErrorCode != null)
        Console.Error.WriteLine($"  Code: {err.ErrorCode}");
    foreach (var ve in err.Errors ?? [])
        Console.Error.WriteLine($"  [{ve.Field}] {ve.Message}");
    return 1;
}
catch (Exception ex)
{
    Console.Error.WriteLine($"Error: {ex.Message}");
    return 1;
}
finally
{
    try
    {
        Console.WriteLine("Closing project...");
        await client.Job.Close.PostAsync();
        Console.WriteLine("Project closed.");
    }
    catch (Exception closeEx)
    {
        Console.Error.WriteLine($"Warning: failed to close job: {closeEx.Message}");
    }
}

stopwatch.Stop();
Console.WriteLine($"Total time: {stopwatch.Elapsed.TotalSeconds:F2}s");

return 0;


// =================================================================
// Geodesic Geometry
// =================================================================

static (List<(double X, double Y, double Z)> Vertices,
        List<(int A, int B)> Edges,
        HashSet<int> BaseIndices)
    GenerateGeodesicHemisphere(double radius, int frequency)
{
    // -- Icosahedron (vertex-up orientation) -----------------------
    var top = Normalize(0, 1, 0);
    var bottom = Normalize(0, -1, 0);

    var rRing = 2.0 / Math.Sqrt(5);
    var yRing = 1.0 / Math.Sqrt(5);

    var upperRing = new (double X, double Y, double Z)[5];
    var lowerRing = new (double X, double Y, double Z)[5];

    for (var k = 0; k < 5; k++)
    {
        var angleUpper = 2 * Math.PI * k / 5;
        var angleLower = angleUpper + Math.PI / 5;

        upperRing[k] = Normalize(
            rRing * Math.Cos(angleUpper), yRing, rRing * Math.Sin(angleUpper));
        lowerRing[k] = Normalize(
            rRing * Math.Cos(angleLower), -yRing, rRing * Math.Sin(angleLower));
    }

    var icoVerts = new List<(double X, double Y, double Z)> { top };
    icoVerts.AddRange(upperRing);   // indices 1-5
    icoVerts.AddRange(lowerRing);   // indices 6-10
    icoVerts.Add(bottom);           // index 11

    var icoFaces = new List<(int, int, int)>();
    for (var i = 0; i < 5; i++)
    {
        var n = (i + 1) % 5;
        icoFaces.Add((0, 1 + i, 1 + n));       // top cap
        icoFaces.Add((1 + i, 6 + i, 1 + n));   // upper band
        icoFaces.Add((6 + i, 6 + n, 1 + n));   // lower band
        icoFaces.Add((11, 6 + n, 6 + i));       // bottom cap
    }

    // -- Subdivide and project ------------------------------------
    var vertexMap = new Dictionary<(double, double, double), int>();
    var vertexList = new List<(double X, double Y, double Z)>();
    var edgeSet = new HashSet<(int, int)>();

    int AddVertex(double x, double y, double z)
    {
        var (nx, ny, nz) = Normalize(x, y, z);
        var key = (Math.Round(nx, 10), Math.Round(ny, 10), Math.Round(nz, 10));
        if (!vertexMap.TryGetValue(key, out var idx))
        {
            idx = vertexList.Count;
            vertexMap[key] = idx;
            vertexList.Add((nx, ny, nz));
        }
        return idx;
    }

    void AddEdge(int a, int b) => edgeSet.Add(a < b ? (a, b) : (b, a));

    foreach (var (f0, f1, f2) in icoFaces)
    {
        var v0 = icoVerts[f0];
        var v1 = icoVerts[f1];
        var v2 = icoVerts[f2];

        var grid = new Dictionary<(int, int), int>();
        for (var i = 0; i <= frequency; i++)
        {
            for (var j = 0; j <= frequency - i; j++)
            {
                var wi = (double)i / frequency;
                var wj = (double)j / frequency;
                var w0 = 1.0 - wi - wj;
                grid[(i, j)] = AddVertex(
                    w0 * v0.X + wi * v1.X + wj * v2.X,
                    w0 * v0.Y + wi * v1.Y + wj * v2.Y,
                    w0 * v0.Z + wi * v1.Z + wj * v2.Z);
            }
        }

        for (var i = 0; i < frequency; i++)
        {
            for (var j = 0; j < frequency - i; j++)
            {
                var a = grid[(i, j)];
                var b = grid[(i + 1, j)];
                var c = grid[(i, j + 1)];
                AddEdge(a, b);
                AddEdge(b, c);
                AddEdge(a, c);
                if (i + j + 1 < frequency)
                {
                    var d = grid[(i + 1, j + 1)];
                    AddEdge(b, d);
                    AddEdge(c, d);
                }
            }
        }
    }

    // -- Hemisphere filter ----------------------------------------
    var tolerance = 0.6 / frequency;
    var keep = new Dictionary<int, int>();
    var vertices = new List<(double X, double Y, double Z)>();
    var baseIndices = new HashSet<int>();

    for (var oldIdx = 0; oldIdx < vertexList.Count; oldIdx++)
    {
        var (nx, ny, nz) = vertexList[oldIdx];
        if (ny < -tolerance) continue;

        if (ny < tolerance)
            ny = 0.0;

        int newIdx;
        if (ny == 0.0)
        {
            var rXz = Math.Sqrt(nx * nx + nz * nz);
            if (rXz > 1e-12)
            {
                vertices.Add((nx / rXz * radius, 0.0, nz / rXz * radius));
            }
            else
            {
                vertices.Add((nx * radius, 0.0, nz * radius));
            }
            newIdx = vertices.Count - 1;
            baseIndices.Add(newIdx);
        }
        else
        {
            vertices.Add((nx * radius, ny * radius, nz * radius));
            newIdx = vertices.Count - 1;
        }
        keep[oldIdx] = newIdx;
    }

    var edges = new List<(int A, int B)>();
    foreach (var (a, b) in edgeSet)
    {
        if (keep.TryGetValue(a, out var na) && keep.TryGetValue(b, out var nb))
            edges.Add((na, nb));
    }

    return (vertices, edges, baseIndices);
}

static (double X, double Y, double Z) Normalize(double x, double y, double z)
{
    var len = Math.Sqrt(x * x + y * y + z * z);
    return (x / len, y / len, z / len);
}
