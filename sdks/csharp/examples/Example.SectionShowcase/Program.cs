using SpaceGassApi.Models;
using SpaceGassApi.Examples.Common;

// ---------------------------------------------------------------
// Example: Section Showcase
//
// Opens an existing SPACE GASS project that contains sections,
// reads all sections, then creates a grid of member pairs
// — one vertical and one horizontal per section — so you can
// visually inspect every section in both orientations.
//
// Demonstrates:
//   1. Opening an existing project file
//   2. Fetching all sections via GET
//   3. Bulk-creating nodes (3 per section: base, top, end)
//   4. Bulk-creating members (2 per section: vertical + horizontal)
//   5. Saving a copy with SaveAs
//
// Prerequisites:
//   - SPACE GASS API running locally (default: https://localhost:53483)
//   - A valid API key
//   - A SPACE GASS project file (.SG) containing sections
// ---------------------------------------------------------------

// -- Configuration ------------------------------------------------
Console.Write("Enter the path to the SPACE GASS file: ");
var sourceFile = Console.ReadLine()?.Trim().Trim('"');
if (string.IsNullOrWhiteSpace(sourceFile))
{
    Console.WriteLine("No file path provided.");
    return 1;
}

const double memberLength = 0.5;  // metres
const double gridSpacing = 1.0;   // metres between grid positions (room for vertical + horizontal)

var client = ApiClientFactory.Create();

try
{
    // -- Open the existing project --------------------------------
    Console.WriteLine($"Opening: {sourceFile}");
    await client.Job.Open.PostAsync(new OpenJobRequest { FilePath = sourceFile });
    Console.WriteLine("Project opened.");
    Console.WriteLine();

    // -- Fetch all sections ---------------------------------------
    Console.WriteLine("Fetching sections...");
    var sections = await client.Job.Structure.Sections.GetAsync();
    if (sections is null || sections.Count == 0)
    {
        Console.WriteLine("No sections found in the project.");
        return 1;
    }

    Console.WriteLine($"Found {sections.Count} sections:");
    foreach (var sec in sections)
    {
        Console.WriteLine($"  [{sec.Key}] {sec.Name,-30} A={sec.A,10:F2}  Iy={sec.Iy,12:F2}  Source={sec.Source}");
    }
    Console.WriteLine();

    // -- Compute grid dimensions ----------------------------------
    // Lay members out in a rectangular grid with roughly equal rows/cols.
    var count = sections.Count;
    var cols = (int)Math.Ceiling(Math.Sqrt(count));
    var rows = (int)Math.Ceiling((double)count / cols);

    Console.WriteLine($"Grid layout: {cols} columns x {rows} rows ({count} sections, {count * 2} members)");
    Console.WriteLine();

    // -- Build nodes for each section pair ------------------------
    // SPACE GASS uses Y as the vertical axis, so the plan is X-Z.
    // For each section we create 3 nodes at the grid position (X, Z):
    //   Base node:       (x, 0, z)              — shared base
    //   Vertical top:    (x, memberLength, z)    — vertical member goes up along Y
    //   Horizontal end:  (x + memberLength, 0, z) — horizontal member goes along X
    var baseNodes = new List<NodeCreate>(count);
    var topNodes = new List<NodeCreate>(count);
    var endNodes = new List<NodeCreate>(count);

    for (var i = 0; i < count; i++)
    {
        var col = i % cols;
        var row = i / cols;

        var x = col * gridSpacing;
        var z = row * gridSpacing;

        baseNodes.Add(new NodeCreate { X = x, Y = 0.0, Z = z });
        topNodes.Add(new NodeCreate { X = x, Y = memberLength, Z = z });
        endNodes.Add(new NodeCreate { X = x + memberLength, Y = 0.0, Z = z });
    }

    // Combine into a single bulk request: [base..., top..., end...].
    var allNodes = new List<NodeCreate>(count * 3);
    allNodes.AddRange(baseNodes);
    allNodes.AddRange(topNodes);
    allNodes.AddRange(endNodes);

    Console.WriteLine($"Bulk-creating {allNodes.Count} nodes...");
    var nodeResult = await client.Job.Structure.Nodes.Bulk.PostAsync(allNodes);
    var createdNodes = nodeResult!.Succeeded!;

    if (nodeResult.Errors?.Count > 0)
    {
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.WriteLine($"  Warning: {nodeResult.Errors.Count} node(s) had errors.");
        Console.ResetColor();
    }

    Console.WriteLine($"  Created {createdNodes.Count} nodes.");

    // Split the created nodes back into base, top, and end groups.
    var createdBase = createdNodes.GetRange(0, count);
    var createdTop = createdNodes.GetRange(count, count);
    var createdEnd = createdNodes.GetRange(count * 2, count);

    // -- Build member pairs, each with the same section ------------
    // Two members per section: one vertical (base->top), one horizontal (base->end).
    var memberCreateList = new List<MemberCreate>(count * 2);

    for (var i = 0; i < count; i++)
    {
        var sectionKey = sections[i].Key!.Value;
        var baseKey = createdBase[i].Key!.Value;

        // Vertical member (along Y)
        memberCreateList.Add(new MemberCreate
        {
            NodeA = baseKey,
            NodeB = createdTop[i].Key!.Value,
            Section = sectionKey
        });

        // Horizontal member (along X)
        memberCreateList.Add(new MemberCreate
        {
            NodeA = baseKey,
            NodeB = createdEnd[i].Key!.Value,
            Section = sectionKey
        });
    }

    Console.WriteLine($"Bulk-creating {memberCreateList.Count} members...");
    var memberResult = await client.Job.Structure.Members.Bulk.PostAsync(memberCreateList);
    var createdMembers = memberResult!.Succeeded!;

    if (memberResult.Errors?.Count > 0)
    {
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.WriteLine($"  Warning: {memberResult.Errors.Count} member(s) had errors.");
        Console.ResetColor();
    }

    Console.WriteLine($"  Created {createdMembers.Count} members.");
    Console.WriteLine();

    // -- Print summary --------------------------------------------
    Console.WriteLine("Member -> Section mapping:");
    for (var i = 0; i < createdMembers.Count; i += 2)
    {
        var vertical = createdMembers[i];
        var horizontal = createdMembers[i + 1];
        var sec = sections.FirstOrDefault(s => s.Key == vertical.Section);
        Console.WriteLine($"  Section [{vertical.Section}] {sec?.Name,-30}  Vertical=M{vertical.Key}  Horizontal=M{horizontal.Key}");
    }
    Console.WriteLine();

    // -- SaveAs with a postfix ------------------------------------
    var dir = Path.GetDirectoryName(sourceFile)!;
    var name = Path.GetFileNameWithoutExtension(sourceFile);
    var ext = Path.GetExtension(sourceFile);
    var saveFile = Path.Combine(dir, $"{name}_SectionShowcase{ext}");

    Console.WriteLine($"Saving as: {saveFile}");
    await client.Job.Save.PostAsync(new SaveJobRequest { FilePath = saveFile });
    Console.WriteLine("Saved.");

    // -- Close ----------------------------------------------------
    Console.WriteLine("Closing project...");
    await client.Job.Close.PostAsync();
    Console.WriteLine("Done.");
}
catch (Exception ex)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Error.WriteLine($"Error: {ex.Message}");
    Console.ResetColor();
    return 1;
}

return 0;
