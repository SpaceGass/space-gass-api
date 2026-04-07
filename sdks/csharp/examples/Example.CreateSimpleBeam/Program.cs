using SpaceGassApi.Job.New;
using SpaceGassApi.Models;
using SpaceGassApi.Examples.Common;

// ---------------------------------------------------------------
// Example: Create a Simple Beam Model from Scratch
//
// Demonstrates how to:
//   1. Create a new blank SPACE GASS project
//   2. Add two nodes
//   3. Apply restraints (fixed + pinned)
//   4. Create a beam member between the nodes
//
// Prerequisites:
//   - SPACE GASS API running locally (default: https://localhost:53483)
//   - A valid API key
// ---------------------------------------------------------------

// -- Configuration ------------------------------------------------
var saveFilePath = Path.Combine(
    Environment.GetFolderPath(Environment.SpecialFolder.Desktop),
    "SpaceGass Examples",
    "SimpleBeam.sg");

var client = ApiClientFactory.Create();

try
{
    // -- Create a new blank project --------------------------------
    Console.WriteLine("Creating new blank project...");
    await client.Job.New.PostAsync(new NewPostRequestBody());
    Console.WriteLine("New project created.");
    Console.WriteLine();

    // -- Create two nodes ------------------------------------------
    Console.WriteLine("Creating nodes...");

    var node1 = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 0.0, Y = 0.0, Z = 0.0 });
    Console.WriteLine($"  Node {node1?.Key}: ({node1?.X}, {node1?.Y}, {node1?.Z})");

    var node2 = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 6.0, Y = 0.0, Z = 0.0 });
    Console.WriteLine($"  Node {node2?.Key}: ({node2?.X}, {node2?.Y}, {node2?.Z})");
    Console.WriteLine();

    // -- Apply restraints ------------------------------------------
    // Restraint code: 6 characters for TX, TY, TZ, RX, RY, RZ
    //   F = Free, R = Restrained
    Console.WriteLine("Applying restraints...");

    // Node 1: Fixed support (all DOFs restrained)
    await client.Job.Structure.Nodes[node1!.Key!.Value].Restraint.PostAsync(
        new NodeRestraintCreate { RestraintCode = "RRRRRR" });
    Console.WriteLine($"  Node {node1.Key}: Fixed (RRRRRR)");

    // Node 2: Pinned support (translations restrained, rotations free)
    await client.Job.Structure.Nodes[node2!.Key!.Value].Restraint.PostAsync(
        new NodeRestraintCreate { RestraintCode = "RRRFFF" });
    Console.WriteLine($"  Node {node2.Key}: Pinned (RRRFFF)");
    Console.WriteLine();

    // -- Create a beam member between the two nodes ----------------
    Console.WriteLine("Creating beam member...");

    var member = await client.Job.Structure.Members.PostAsync(
        new MemberCreate
        {
            NodeA = node1.Key.Value,
            NodeB = node2.Key.Value
        });
    Console.WriteLine($"  Member {member?.Key}: Node {member?.NodeA} -> Node {member?.NodeB}");
    Console.WriteLine();

    // -- Summary ---------------------------------------------------
    Console.WriteLine("Simple beam model created successfully!");
    Console.WriteLine($"  Nodes:   {node1.Key}, {node2.Key}");
    Console.WriteLine($"  Members: {member?.Key}");
    Console.WriteLine($"  Span:    6.0 (length units)");

    // -- Save the project ------------------------------------------
    // New jobs must use SaveAs to establish a file path.
    Console.WriteLine();
    Console.WriteLine($"Saving project to: {saveFilePath}");
    await client.Job.Save.PostAsync(new SaveJobRequest { FilePath = saveFilePath });
    Console.WriteLine("Project saved.");

    // -- Close the project -----------------------------------------
    Console.WriteLine();
    Console.WriteLine("Closing project...");
    await client.Job.Close.PostAsync();
    Console.WriteLine("Project closed.");
}
catch (Exception ex)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Error.WriteLine($"Error: {ex.Message}");
    Console.ResetColor();
    return 1;
}

return 0;
