using SpaceGassApi;
using SpaceGassApi.Models;
using SpaceGassApi.Utils;


// ---------------------------------------------------------------
// Example: Create a Simple Plate Model from Scratch
//
// Builds a 2 m wide x 10 m long simply-supported plate slab:
//   1.  Create the client and a new project
//   2.  Add a user-defined material (25 MPa concrete)
//   3.  Bulk-create a rectangular grid of nodes (0.5 m spacing)
//   4.  Apply restraints along the short edges
//       - Pinned  (FFFRRR) at X = 0
//       - Roller  (RFRRRR) at X = 10
//   5.  Bulk-create quad plate elements across the grid
//   6.  Check the errors log for engine-level diagnostics
//   7.  Add plate cuts at the supports and midspan
//   8.  Create load cases and combinations (same as SimpleBeam)
//   9.  Apply self-weight and plate pressure loads
//   10. Save the model
//   11. Run a linear static analysis and wait for completion
//   12. Query reactions
//   13. Save the analysed model and close
//
// Prerequisites:
//   - SPACE GASS API running locally (default: http://localhost:34560)
// ---------------------------------------------------------------

// -- Configuration ------------------------------------------------
const double SpanLength = 10.0;   // metres (X direction)
const double PlateWidth = 2.0;    // metres (Z direction)
const double ElementSize = 0.5;   // metres (mesh spacing)
const double Thickness = 0.2;     // metres (200 mm slab)

var saveFilePath = Path.Combine(
    Environment.GetFolderPath(Environment.SpecialFolder.Desktop),
    "SpaceGass Examples",
    "SimplePlate.sg");

var client = SpaceGassApiClient.CreateClient("http://localhost:34560");

try
{
    // == Step 1 — Create a new blank project =======================
    Console.WriteLine("Creating new blank project...");
    await client.Job.New.PostAsync();
    Console.WriteLine("New project created.");
    Console.WriteLine();

    // == Step 2 — Add a user-defined material =====================
    Console.WriteLine("Adding 25 MPa concrete material...");
    var concrete = await client.Job.Structure.Materials.PostAsync(
        new MaterialUserCreate
        {
            Name = "25 MPa Concrete",
            YoungsModulus = 26700.0,       // MPa
            PoissonsRatio = 0.2,
            MassDensity = 2400.0,          // kg/m³
            ThermalCoeff = 1.0e-5,         // per °C
            ConcreteStrength = 25.0,       // MPa
        });
    Console.WriteLine($"  Material {concrete!.Id}: {concrete.Name}");
    Console.WriteLine();

    // == Step 3 — Bulk-create nodes ===============================
    // Rectangular grid: X from 0..10 m, Z from 0..2 m
    var nX = (int)(SpanLength / ElementSize) + 1;   // 21 nodes along X
    var nZ = (int)(PlateWidth / ElementSize) + 1;    // 5 nodes across Z

    Console.WriteLine($"Creating {nX} x {nZ} = {nX * nZ} node grid (bulk)...");

    var nodeCreates = new List<NodeCreate>();
    for (var ix = 0; ix < nX; ix++)
    {
        for (var iz = 0; iz < nZ; iz++)
        {
            nodeCreates.Add(new NodeCreate
            {
                X = ix * ElementSize,
                Y = 0.0,
                Z = iz * ElementSize,
            });
        }
    }

    var nodeResult = await client.Job.Structure.Nodes.Bulk.PostAsync(nodeCreates);
    var createdNodes = nodeResult!.Succeeded!;
    Console.WriteLine($"  {createdNodes.Count} nodes created");

    if (nodeResult.Errors is { Count: > 0 } nodeErrors)
    {
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.Error.WriteLine($"  WARNING: {nodeErrors.Count} node(s) failed:");
        foreach (var e in nodeErrors)
            Console.Error.WriteLine($"    [{e.Index}] {e.Error}");
        Console.ResetColor();
    }

    // Build a lookup: [ix, iz] → node Id
    var nodeId = new int[nX, nZ];
    var idx = 0;
    for (var ix = 0; ix < nX; ix++)
    {
        for (var iz = 0; iz < nZ; iz++)
        {
            nodeId[ix, iz] = createdNodes[idx++].Id!.Value;
        }
    }
    Console.WriteLine();

    // == Step 4 — Apply restraints along the short edges ==========
    // Pinned at X = 0  (all translations fixed, rotations free)
    // Roller at X = 10 (only TY fixed — free to slide in X and Z)
    Console.WriteLine("Applying restraints...");

    var restraintCreates = new List<NodeRestraintCreate>();

    for (var iz = 0; iz < nZ; iz++)
    {
        // Pinned edge (X = 0)
        restraintCreates.Add(new NodeRestraintCreate
        {
            Node = nodeId[0, iz],
            RestraintCode = "FFFRRR",
        });

        // Roller edge (X = 10)
        restraintCreates.Add(new NodeRestraintCreate
        {
            Node = nodeId[nX - 1, iz],
            RestraintCode = "RFRRRR",
        });
    }

    var restraintResult = await client.Job.Structure.NodeRestraints.Bulk.PostAsync(
        restraintCreates);
    Console.WriteLine($"  {restraintResult!.Succeeded!.Count} restraints applied");

    if (restraintResult.Errors is { Count: > 0 } restraintErrors)
    {
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.Error.WriteLine($"  WARNING: {restraintErrors.Count} restraint(s) failed:");
        foreach (var e in restraintErrors)
            Console.Error.WriteLine($"    [{e.Index}] {e.Error}");
        Console.ResetColor();
    }
    Console.WriteLine();

    // == Step 5 — Bulk-create quad plate elements ==================
    // Each plate spans a 0.5 x 0.5 m cell in the grid.
    // Node winding: A(ix,iz) → B(ix+1,iz) → C(ix+1,iz+1) → D(ix,iz+1)
    var plateCountX = nX - 1;   // 20
    var plateCountZ = nZ - 1;   // 4

    Console.WriteLine($"Creating {plateCountX * plateCountZ} plate elements (bulk)...");

    var plateCreates = new List<PlateCreate>();
    for (var ix = 0; ix < plateCountX; ix++)
    {
        for (var iz = 0; iz < plateCountZ; iz++)
        {
            plateCreates.Add(new PlateCreate
            {
                NodeA = nodeId[ix, iz],
                NodeB = nodeId[ix + 1, iz],
                NodeC = nodeId[ix + 1, iz + 1],
                NodeD = nodeId[ix, iz + 1],
                Material = concrete.Id,
                ActualThickness = Thickness * 1000,      // mm
                MembraneThickness = Thickness * 1000,
                BendingThickness = Thickness * 1000,
                ShearThickness = Thickness * 1000,
                Theory = PlateTheory.Mindlin,
            });
        }
    }

    var plateResult = await client.Job.Structure.Plates.Bulk.PostAsync(plateCreates);
    var createdPlates = plateResult!.Succeeded!;
    Console.WriteLine($"  {createdPlates.Count} plates created");

    if (plateResult.Errors is { Count: > 0 } plateErrors)
    {
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.Error.WriteLine($"  WARNING: {plateErrors.Count} plate(s) failed:");
        foreach (var e in plateErrors)
            Console.Error.WriteLine($"    [{e.Index}] {e.Error}");
        Console.ResetColor();
    }

    if (createdPlates.Count == 0)
    {
        throw new Exception("No plates were created. Cannot continue.");
    }
    Console.WriteLine();

    // == Step 6 — Check the errors log ============================
    // The errors endpoint returns engine-level diagnostic messages
    // logged during the session. Check it after creating plates to
    // catch issues that the bulk result may not surface.
    Console.WriteLine("Checking errors log...");
    var errors = await client.Job.Errors.GetAsync();

    if (errors!.Count > 0)
    {
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.Error.WriteLine($"  {errors.Count} engine message(s):");
        foreach (var msg in errors.Errors!)
            Console.Error.WriteLine($"    {msg}");
        Console.ResetColor();
    }
    else
    {
        Console.WriteLine("  No errors.");
    }
    Console.WriteLine();

    // Build a lookup: [ix, iz] → plate Id
    var plateId = new int[plateCountX, plateCountZ];
    idx = 0;
    for (var ix = 0; ix < plateCountX; ix++)
    {
        for (var iz = 0; iz < plateCountZ; iz++)
        {
            plateId[ix, iz] = createdPlates[idx++].Id!.Value;
        }
    }

    // == Step 7 — Add plate cuts ==================================
    // Three transverse cuts across the full plate width:
    //   - Just inside the left support  (X = 0.5 m)
    //   - At midspan                    (X = 5.0 m)
    //   - Just inside the right support (X = 9.5 m)
    //
    // Each cut line runs from Z = 0 to Z = 2, which passes through
    // plates in the same X-column. We specify start/end plates as
    // the first and last plate in that column, and start/end nodes
    // at Z = 0 and Z = 2 on the cut X-coordinate.
    Console.WriteLine("Adding plate cuts...");

    var cutDefinitions = new (string Title, int Ix, double CutX)[]
    {
        ("Left support (X=0.5m)",  1, 0.5),
        ("Midspan (X=5.0m)",       10, 5.0),
        ("Right support (X=9.5m)", 19, 9.5),
    };

    var cutCreates = new List<PlateCutCreate>();
    foreach (var (title, cutIx, cutX) in cutDefinitions)
    {
        // The cut passes through the column of plates at index cutIx-1
        // (plate column index is 0-based, cutIx is the node column).
        // But the cut line is along the right edge of column cutIx-1,
        // which means it starts at the first plate in that column and
        // ends at the last plate in that column.
        var startPlate = plateId[cutIx - 1, 0];             // bottom plate in the column
        var endPlate = plateId[cutIx - 1, plateCountZ - 1]; // top plate in the column

        // The start/end nodes define the line: Z=0 to Z=2 at X=cutX
        var startNode = nodeId[cutIx, 0];
        var endNode = nodeId[cutIx, nZ - 1];

        cutCreates.Add(new PlateCutCreate
        {
            Title = title,
            StartPlate = startPlate,
            EndPlate = endPlate,
            StartNode = startNode,
            EndNode = endNode,
        });
    }

    var cutResult = await client.Job.Structure.PlateCuts.Bulk.PostAsync(cutCreates);
    Console.WriteLine($"  {cutResult!.Succeeded!.Count} plate cuts created");

    if (cutResult.Errors is { Count: > 0 } cutErrors)
    {
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.Error.WriteLine($"  WARNING: {cutErrors.Count} plate cut(s) failed:");
        foreach (var e in cutErrors)
            Console.Error.WriteLine($"    [{e.Index}] {e.Error}");
        Console.ResetColor();
    }
    Console.WriteLine();

    // == Step 8 — Create primary load cases ========================
    Console.WriteLine("Creating primary load cases...");
    var selfWeightCase = await client.Job.Loads.LoadCases.PostAsync(
        new LoadCaseCreate { Id = 1, Title = "Self-weight" });
    var deadCase = await client.Job.Loads.LoadCases.PostAsync(
        new LoadCaseCreate { Id = 2, Title = "Dead Load" });
    var liveCase = await client.Job.Loads.LoadCases.PostAsync(
        new LoadCaseCreate { Id = 3, Title = "Live Load" });
    Console.WriteLine($"  Cases: SW={selfWeightCase!.Id}, G={deadCase!.Id}, Q={liveCase!.Id}");
    Console.WriteLine();

    // == Step 9 — Apply the self-weight load =======================
    Console.WriteLine("Applying self-weight load...");
    await client.Job.Loads.SelfWeightLoads.PostAsync(
        new SelfWeightLoadCreate
        {
            LoadCase = selfWeightCase.Id,
            AccelerationX = 0.0,
            AccelerationY = -1.0,
            AccelerationZ = 0.0,
        });
    Console.WriteLine();

    // == Step 10 — Apply plate pressure loads ======================
    // Dead load: 1.0 kPa superimposed dead load (on top of self-weight)
    // Live load: 3.0 kPa (typical floor live load)
    Console.WriteLine("Applying plate pressure loads...");

    var pressureLoads = new List<PlatePressureLoadCreate>();
    foreach (var plate in createdPlates)
    {
        // Dead load — 1.0 kPa downward
        pressureLoads.Add(new PlatePressureLoadCreate
        {
            LoadCase = deadCase.Id,
            Plate = plate.Id,
            Axes = LoadAxes.GlobalProjected,
            Px = 0.0,
            Py = -1.0,     // kPa
            Pz = 0.0,
        });

        // Live load — 3.0 kPa downward
        pressureLoads.Add(new PlatePressureLoadCreate
        {
            LoadCase = liveCase.Id,
            Plate = plate.Id,
            Axes = LoadAxes.GlobalProjected,
            Px = 0.0,
            Py = -3.0,     // kPa
            Pz = 0.0,
        });
    }

    await client.Job.Loads.PlatePressureLoads.Bulk.PostAsync(pressureLoads);
    Console.WriteLine($"  {pressureLoads.Count} pressure loads applied");
    Console.WriteLine();

    // == Step 11 — ULS and SLS combinations ========================
    Console.WriteLine("Defining ULS and SLS combinations to AS/NZS 1170...");

    var ulsCase = await client.Job.Loads.CombinationLoadCases.PostAsync(
        new CombinationLoadCaseCreate
        {
            Id = 10,
            Title = "ULS - Strength",
            CombinationItems = new List<CombinationLoadCaseItem>
            {
                new() { LoadCase = selfWeightCase.Id, MultiplyingFactor = 1.2 },
                new() { LoadCase = deadCase.Id,       MultiplyingFactor = 1.2 },
                new() { LoadCase = liveCase.Id,       MultiplyingFactor = 1.5 },
            },
        });

    var slsCase = await client.Job.Loads.CombinationLoadCases.PostAsync(
        new CombinationLoadCaseCreate
        {
            Id = 20,
            Title = "SLS - Short-term Deflection",
            CombinationItems = new List<CombinationLoadCaseItem>
            {
                new() { LoadCase = selfWeightCase.Id, MultiplyingFactor = 1.0 },
                new() { LoadCase = deadCase.Id,       MultiplyingFactor = 1.0 },
                new() { LoadCase = liveCase.Id,       MultiplyingFactor = 0.7 },
            },
        });

    Console.WriteLine($"  ULS  case Id = {ulsCase!.Id}");
    Console.WriteLine($"  SLS  case Id = {slsCase!.Id}");
    Console.WriteLine();

    // == Step 12 — Save the initial model ==========================
    Console.WriteLine($"Saving initial model to: {saveFilePath}");
    await client.Job.Save.PostAsync(
        new SaveJobRequest { FilePath = saveFilePath });
    Console.WriteLine("Model saved.");
    Console.WriteLine();

    // == Step 13 — Run a linear static analysis ====================
    Console.WriteLine("Configuring static analysis settings...");
    await client.Job.Analysis.Static.Settings.PatchAsync(
        new StaticSettingsUpdate
        {
            SolverType = SolverType.Paradise,
        });

    Console.WriteLine("Running linear static analysis...");
    var run = await client.Job.Analysis.Static.RunLinear.PostAsync(
        new StaticSettingsUpdate());
    Console.WriteLine($"  Run {run!.RunId} queued; waiting for completion...");

    AnalysisRun finalRun;
    while (true)
    {
        await Task.Delay(500);
        finalRun = (await client.Job.Analysis.Runs[run.RunId!.Value].GetAsync())!;
        if (finalRun.Status is AnalysisRunStatus.Completed
                            or AnalysisRunStatus.Failed
                            or AnalysisRunStatus.Cancelled)
        {
            break;
        }
    }

    Console.WriteLine($"  Analysis {finalRun.Status} in {finalRun.ElapsedTime}");
    if (finalRun.Status != AnalysisRunStatus.Completed)
    {
        throw new Exception($"Analysis did not complete: {finalRun.ErrorMessage}");
    }
    Console.WriteLine();

    // == Step 14 — Query reactions =================================
    Console.WriteLine("Querying ULS reactions...");
    var reactions = await client.Job.Query.Analysis.Static.NodeReactions.GetAsync(config =>
    {
        config.QueryParameters.LoadCases = new[] { ulsCase.Id!.Value }.ToFilterString();
    });

    Console.WriteLine($"  {"Node",-8} {"Fx",12} {"Fy",12} {"Fz",12} {"Mx",12} {"My",12} {"Mz",12}");
    Console.WriteLine($"  {new string('-', 80)}");
    foreach (var r in reactions!.Results!)
    {
        Console.WriteLine($"  {r.Node,-8} {r.Fx,12:F4} {r.Fy,12:F4} {r.Fz,12:F4} {r.Mx,12:F4} {r.My,12:F4} {r.Mz,12:F4}");
    }
    Console.WriteLine();

    // == Step 15 — Save the analysed model =========================
    Console.WriteLine($"Saving analysed model to: {saveFilePath}");
    await client.Job.Save.PostAsync(new SaveJobRequest { FilePath = saveFilePath });
    Console.WriteLine("Project saved.");
}
catch (ErrorResponse err)
{
    // Structured API error (validation failures, not-found, etc.)
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Error.WriteLine($"API error {err.Status}: {err.Title}");
    if (!string.IsNullOrWhiteSpace(err.Detail))
        Console.Error.WriteLine($"  {err.Detail}");
    if (!string.IsNullOrWhiteSpace(err.ErrorCode))
        Console.Error.WriteLine($"  Code: {err.ErrorCode}");
    foreach (var ve in err.Errors ?? [])
        Console.Error.WriteLine($"  [{ve.Field}] {ve.Message}");
    Console.ResetColor();
    return 1;
}
catch (Exception ex)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Error.WriteLine($"Error: {ex.Message}");
    Console.ResetColor();
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
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.Error.WriteLine($"Warning: failed to close job: {closeEx.Message}");
        Console.ResetColor();
    }
}

return 0;
