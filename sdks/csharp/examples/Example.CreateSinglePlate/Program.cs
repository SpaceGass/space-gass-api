using SpaceGassApi;
using SpaceGassApi.Models;


// ---------------------------------------------------------------
// Example: Create a Single Plate
//
// Bare-minimum example that creates one quad plate element:
//   1. New project
//   2. Four nodes (1 m x 1 m square)
//   3. One material
//   4. One plate
//   5. Check errors log
//   6. Save and close
// ---------------------------------------------------------------

var saveFilePath = Path.Combine(
    Environment.GetFolderPath(Environment.SpecialFolder.Desktop),
    "SpaceGass Examples",
    "SinglePlate.sg");

var client = SpaceGassApiClient.CreateClient("http://localhost:34560");

try
{
    // == New project ===============================================
    Console.WriteLine("Creating new blank project...");
    await client.Job.New.PostAsync();
    Console.WriteLine("Done.");
    Console.WriteLine();

    // == Four corner nodes (1 m x 1 m in the XZ plane) ============
    Console.WriteLine("Creating 4 nodes...");

    var n1 = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 0.0, Y = 0.0, Z = 0.0 });
    Console.WriteLine($"  Node {n1!.Id}: ({n1.X}, {n1.Y}, {n1.Z})");

    var n2 = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 1.0, Y = 0.0, Z = 0.0 });
    Console.WriteLine($"  Node {n2!.Id}: ({n2.X}, {n2.Y}, {n2.Z})");

    var n3 = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 1.0, Y = 0.0, Z = 1.0 });
    Console.WriteLine($"  Node {n3!.Id}: ({n3.X}, {n3.Y}, {n3.Z})");

    var n4 = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 0.0, Y = 0.0, Z = 1.0 });
    Console.WriteLine($"  Node {n4!.Id}: ({n4.X}, {n4.Y}, {n4.Z})");
    Console.WriteLine();

    // == Material =================================================
    Console.WriteLine("Adding material...");
    var mat = await client.Job.Structure.Materials.PostAsync(
        new MaterialCreate
        {
            Name = "Concrete 25 MPa",
            YoungsModulus = 26700.0,
            PoissonsRatio = 0.2,
            MassDensity = 2400.0,
            ThermalCoeff = 1.0e-5,
            ConcreteStrength = 25.0,
        });
    Console.WriteLine($"  Material {mat!.Id}: {mat.Name}");
    Console.WriteLine();

    // == Single plate =============================================
    Console.WriteLine("Creating plate...");
    var plate = await client.Job.Structure.Plates.PostAsync(
        new PlateCreate
        {
            NodeA = n1.Id,
            NodeB = n2.Id,
            NodeC = n3.Id,
            NodeD = n4.Id,
            Material = mat.Id,
            ActualThickness = 200.0,       // mm
            MembraneThickness = 200.0,
            BendingThickness = 200.0,
            ShearThickness = 200.0,
            Theory = PlateTheory.Mindlin,
        });
    Console.WriteLine($"  Plate {plate!.Id}: nodes [{plate.NodeA},{plate.NodeB},{plate.NodeC},{plate.NodeD}]");
    Console.WriteLine();

    // == Verify plate exists via GET ==============================
    Console.WriteLine("Querying plates...");
    var plates = await client.Job.Structure.Plates.GetAsync();
    Console.WriteLine($"  {plates!.Count} plate(s) returned:");
    foreach (var p in plates)
    {
        Console.WriteLine($"    Plate {p.Id}: nodes [{p.NodeA},{p.NodeB},{p.NodeC},{p.NodeD}], " +
                          $"material={p.Material}, thickness={p.ActualThickness}, theory={p.Theory}");
    }
    Console.WriteLine();

    // == Check errors log =========================================
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

    // == Save =====================================================
    Console.WriteLine($"Saving to: {saveFilePath}");
    await client.Job.Save.PostAsync(
        new SaveJobRequest { FilePath = saveFilePath });
    Console.WriteLine("Saved.");
}
catch (ErrorResponse err)
{
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
        Console.WriteLine("Closed.");
    }
    catch (Exception closeEx)
    {
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.Error.WriteLine($"Warning: failed to close job: {closeEx.Message}");
        Console.ResetColor();
    }
}

return 0;
