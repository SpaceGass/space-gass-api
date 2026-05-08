// ---------------------------------------------------------------
// Example: Quick Start
//
// The end-to-end snippet from the docs Quick Start guide as a
// runnable program. Opens a built-in SPACE GASS sample, lists every
// node, then closes the job. No project file of your own required.
//
// Prerequisites:
//   - SPACE GASS API service running locally (default
//     http://localhost:34560/api/v1).
//   - The "Portal Frame.SG" sample is shipped with every install,
//     but you can list available samples via GET /file/samples or
//     in Swagger.
// ---------------------------------------------------------------

using SpaceGassApi;
using SpaceGassApi.Models;

var client = SpaceGassApiClient.CreateClient();

try
{
    Console.WriteLine("Opening sample 'Portal Frame.SG'...");
    await client.Job.OpenSample.PostAsync(
        new OpenSampleRequest { FileName = "Portal Frame.SG" });

    var nodes = await client.Job.Structure.Nodes.GetAsync();
    Console.WriteLine($"Found {nodes!.Count} node(s):");
    foreach (var node in nodes)
    {
        Console.WriteLine($"  Node {node.Id}: ({node.X}, {node.Y}, {node.Z})");
    }
}
catch (ProblemDetails pd)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Error.WriteLine($"API error {pd.Status}: {pd.Title}");
    if (!string.IsNullOrWhiteSpace(pd.Detail))
        Console.Error.WriteLine($"  {pd.Detail}");
    Console.ResetColor();
    return 1;
}
finally
{
    Console.WriteLine("Closing project...");
    await client.Job.Close.PostAsync();
}

return 0;
