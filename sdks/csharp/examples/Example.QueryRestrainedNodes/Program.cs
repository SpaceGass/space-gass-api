using SpaceGassApi;
using SpaceGassApi.Models;


// ---------------------------------------------------------------
// Example: Query Restrained Nodes and Their Reactions
//
// Demonstrates how to:
//   1. Open an existing SPACE GASS project
//   2. Filter nodes to only those with restraints
//   3. Retrieve reaction results for the restrained nodes
//   4. Display the results in a formatted table
//
// Prerequisites:
//   - SPACE GASS API running locally (default: http://localhost:34560)
//   - A valid API key
//   - An existing .sg project file that has been analysed
// ---------------------------------------------------------------

// -- Configuration ------------------------------------------------
// Update these values to match your local environment.
const string projectFilePath = @"C:\Path\To\Your\Project.sg";

var client = SpaceGassApiClient.CreateClient();

try
{
    // -- Open the project ------------------------------------------
    Console.WriteLine($"Opening project: {projectFilePath}");
    await client.Job.Open.PostAsync(new OpenJobRequest { FilePath = projectFilePath });
    Console.WriteLine("Project opened successfully.");
    Console.WriteLine();

    // -- Get restrained nodes --------------------------------------
    Console.WriteLine("Querying restrained nodes...");

    var restrainedNodes = await client.Job.Structure.Nodes.GetAsync(config =>
        config.QueryParameters.NodeTypeAsNodeTypeFilter = NodeTypeFilter.Restrained);

    if (restrainedNodes is null || restrainedNodes.Count == 0)
    {
        Console.WriteLine("  No restrained nodes found in this project.");
    }
    else
    {
        Console.WriteLine($"  Found {restrainedNodes.Count} restrained node(s):");
        Console.WriteLine();
        Console.WriteLine($"  {"Node",-8} {"X",12} {"Y",12} {"Z",12}");
        Console.WriteLine($"  {new string('-', 8)} {new string('-', 12)} {new string('-', 12)} {new string('-', 12)}");

        foreach (var node in restrainedNodes)
        {
            Console.WriteLine($"  {node.Id,-8} {node.X,12:F3} {node.Y,12:F3} {node.Z,12:F3}");
        }

        // -- Get reactions for restrained nodes --------------------
        Console.WriteLine();
        Console.WriteLine("Retrieving reactions for restrained nodes...");

        // Nodes filter uses SG list format (e.g. "1,5-10") — comma-separated Ids works for an arbitrary set.
        var nodeFilter = string.Join(",", restrainedNodes.Where(n => n.Id != null).Select(n => n.Id!.Value));

        var reactionResult = await client.Job.Query.Analysis.Static.NodeReactions.GetAsync(config =>
            config.QueryParameters.Nodes = nodeFilter);

        var reactions = reactionResult?.Results;

        if (reactions is null || reactions.Count == 0)
        {
            Console.WriteLine("  No reaction results found. Has the model been analysed?");
        }
        else
        {
            Console.WriteLine($"  Found {reactions.Count} reaction result(s):");
            Console.WriteLine();
            Console.WriteLine($"  {"Node",-8} {"Case",-8} {"Fx",12} {"Fy",12} {"Fz",12} {"Mx",12} {"My",12} {"Mz",12}");
            Console.WriteLine($"  {new string('-', 8)} {new string('-', 8)} {new string('-', 12)} {new string('-', 12)} {new string('-', 12)} {new string('-', 12)} {new string('-', 12)} {new string('-', 12)}");

            foreach (var r in reactions)
            {
                Console.WriteLine($"  {r.Node,-8} {r.Case,-8} {r.Fx,12:F3} {r.Fy,12:F3} {r.Fz,12:F3} {r.Mx,12:F3} {r.My,12:F3} {r.Mz,12:F3}");
            }
        }
    }

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
