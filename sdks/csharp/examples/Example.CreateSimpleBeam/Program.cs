using SpaceGassApi;
using SpaceGassApi.Models;


// ---------------------------------------------------------------
// Example: Create a Simple Beam Model from Scratch
//
// Mirrors the Simple Beam walkthrough in the Zudoku docs site:
//   1.  Create the client and a new project
//   2.  Create the two nodes
//   3.  Apply restraints (fixed + pinned)
//   4.  Add a material
//   5.  Add a library section
//   6.  Create the member, wired to the section + material
//   7.  Create three primary load cases (self-weight, dead, live)
//   8.  Apply the self-weight load
//   9.  Apply a member distributed load to the dead case
//   10. Apply a member distributed load to the live case
//   11. Define ULS and SLS combinations to AS/NZS 1170
//   12. Run a linear static analysis and wait for completion
//   13. Query reactions under the ULS combination
//   14. Get the maximum ULS bending moment along the beam
//   15. Get the maximum SLS deflection along the beam
//   16. Save and close
//
// Prerequisites:
//   - SPACE GASS API running locally (default: http://localhost:34560)
//   - The "Aust300" section library installed (default in SPACE GASS)
// ---------------------------------------------------------------

// -- Configuration ------------------------------------------------
var saveFilePath = Path.Combine(
    Environment.GetFolderPath(Environment.SpecialFolder.Desktop),
    "SpaceGass Examples",
    "SimpleBeam.sg");

var client = SpaceGassApiClient.CreateClient();

try
{
    // == Step 1 — Create a new blank project =======================
    Console.WriteLine("Creating new blank project...");
    await client.Job.New.PostAsync();
    Console.WriteLine("New project created.");
    Console.WriteLine();

    // == Step 2 — Create nodes =====================================
    Console.WriteLine("Creating nodes...");

    var node1 = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 0.0, Y = 0.0, Z = 0.0 });
    Console.WriteLine($"  Node {node1!.Id}: ({node1.X}, {node1.Y}, {node1.Z})");

    var node2 = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 6.0, Y = 0.0, Z = 0.0 });
    Console.WriteLine($"  Node {node2!.Id}: ({node2.X}, {node2.Y}, {node2.Z})");
    Console.WriteLine();

    // == Step 3 — Apply restraints =================================
    // Restraint code: 6 characters for TX, TY, TZ, RX, RY, RZ
    //   F = Free, R = Restrained
    Console.WriteLine("Applying restraints...");

    await client.Job.Structure.Nodes[node1.Id!.Value].Restraint.PostAsync(
        new NodeRestraintCreate { RestraintCode = "RRRRRR" });
    Console.WriteLine($"  Node {node1.Id}: Fixed (RRRRRR)");

    await client.Job.Structure.Nodes[node2.Id!.Value].Restraint.PostAsync(
        new NodeRestraintCreate { RestraintCode = "RRRFFF" });
    Console.WriteLine($"  Node {node2.Id}: Pinned (RRRFFF)");
    Console.WriteLine();

    // == Step 4 — Add a material ===================================
    Console.WriteLine("Creating material...");
    var steel = await client.Job.Structure.Materials.PostAsync(
        new MaterialCreate
        {
            Name = "350 Grade Steel",
            YoungsModulus = 200000.0,    // MPa
            PoissonsRatio = 0.3,
            MassDensity = 7850.0,        // kg/m^3
            ThermalCoeff = 1.17e-5,      // per °C
        });
    Console.WriteLine($"  Material {steel!.Id}: {steel.Name}");
    Console.WriteLine();

    // == Step 5 — Add a library section ============================
    Console.WriteLine("Adding library section...");
    var section = await client.Job.Structure.Sections.Library.PostAsync(
        new SectionLibraryCreate
        {
            Library = "Aust300",
            Name = "360 UB 44.7",
            Mark = "B1",
        });
    Console.WriteLine($"  Section {section!.Id}: {section.Name}");
    Console.WriteLine();

    // == Step 6 — Create the member ================================
    Console.WriteLine("Creating beam member...");
    var member = await client.Job.Structure.Members.PostAsync(
        new MemberCreate
        {
            NodeA = node1.Id,
            NodeB = node2.Id,
            Section = section.Id,
            Material = steel.Id,
        });
    Console.WriteLine($"  Member {member!.Id}: Node {member.NodeA} -> Node {member.NodeB}");
    Console.WriteLine();

    // == Step 7 — Create primary load cases ========================
    Console.WriteLine("Creating primary load cases...");
    var selfWeightCase = await client.Job.Loads.LoadCases.PostAsync(
        new LoadCaseCreate { Id = 1, Title = "Self-weight" });
    var deadCase = await client.Job.Loads.LoadCases.PostAsync(
        new LoadCaseCreate { Id = 2, Title = "Dead Load" });
    var liveCase = await client.Job.Loads.LoadCases.PostAsync(
        new LoadCaseCreate { Id = 3, Title = "Live Load" });
    Console.WriteLine($"  Cases: SW={selfWeightCase!.Id}, G={deadCase!.Id}, Q={liveCase!.Id}");
    Console.WriteLine();

    // == Step 8 — Apply the self-weight load =======================
    Console.WriteLine("Applying self-weight load...");
    await client.Job.Loads.SelfWeightLoads[selfWeightCase.Id!.Value].PostAsync(
        new SelfWeightLoadCreate
        {
            AccelerationX = 0.0,
            AccelerationY = -9.81,   // m/s² downward
            AccelerationZ = 0.0,
        });
    Console.WriteLine();

    // == Step 9 — Member distributed load on the dead case =========
    Console.WriteLine("Applying 2 kN/m dead load across the span...");
    await client.Job.Loads.MemberDistributedLoads.PostAsync(
        new MemberDistributedLoadCreate
        {
            Case = deadCase.Id,
            Member = member.Id,
            PositionUnits = LoadPositionUnits.Percent,
            StartPosition = 0.0,
            FinishPosition = 100.0,
            FyStart = -2.0,    // kN/m downward
            FyFinish = -2.0,
        });
    Console.WriteLine();

    // == Step 10 — Member distributed load on the live case ========
    Console.WriteLine("Applying 5 kN/m live load across the span...");
    await client.Job.Loads.MemberDistributedLoads.PostAsync(
        new MemberDistributedLoadCreate
        {
            Case = liveCase.Id,
            Member = member.Id,
            PositionUnits = LoadPositionUnits.Percent,
            StartPosition = 0.0,
            FinishPosition = 100.0,
            FyStart = -5.0,
            FyFinish = -5.0,
        });
    Console.WriteLine();

    // == Step 11 — ULS and SLS combinations ========================
    // Combination cases now POST as a single CombinationCaseCreate with
    // CombinationItems inline — one call per combination, no follow-up
    // PUT to set the items.
    Console.WriteLine("Defining ULS and SLS combinations to AS/NZS 1170...");

    var ulsCase = await client.Job.Loads.CombinationLoadCases.PostAsync(
        new CombinationCaseCreate
        {
            Id = 10,
            Title = "ULS - Strength",
            // ULS: 1.2 G + 1.5 Q (self-weight + dead are both G)
            CombinationItems = new List<CombinationItem>
            {
                new() { Case = selfWeightCase.Id, MultiplyingFactor = 1.2 },
                new() { Case = deadCase.Id,       MultiplyingFactor = 1.2 },
                new() { Case = liveCase.Id,       MultiplyingFactor = 1.5 },
            },
        });

    var slsCase = await client.Job.Loads.CombinationLoadCases.PostAsync(
        new CombinationCaseCreate
        {
            Id = 20,
            Title = "SLS - Short-term Deflection",
            // SLS short-term: 1.0 G + 0.7 Q
            CombinationItems = new List<CombinationItem>
            {
                new() { Case = selfWeightCase.Id, MultiplyingFactor = 1.0 },
                new() { Case = deadCase.Id,       MultiplyingFactor = 1.0 },
                new() { Case = liveCase.Id,       MultiplyingFactor = 0.7 },
            },
        });

    Console.WriteLine($"  ULS  case Id = {ulsCase!.Id}");
    Console.WriteLine($"  SLS  case Id = {slsCase!.Id}");
    Console.WriteLine();

    // == Step 12 — Run a linear static analysis ====================
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

    // == Step 13 — Query reactions =================================
    Console.WriteLine("Querying ULS reactions...");
    var reactions = await client.Job.Query.Analysis.Static.Node.Reactions.GetAsync(
        config => config.QueryParameters.Cases = $"{ulsCase.Id}");

    if (reactions!.Warnings?.CasesNotAnalyzed is { Length: > 0 } missing)
    {
        throw new Exception($"Cases not analysed: {missing}. Run the analysis first.");
    }

    foreach (var r in reactions.Results!)
    {
        Console.WriteLine(
            $"  Node {r.Node}, LC {r.Case}: " +
            $"Fx={r.Fx:F2}, Fy={r.Fy:F2}, Fz={r.Fz:F2}");
    }
    Console.WriteLine();

    // == Step 14 — Maximum ULS bending moment ======================
    var ulsForces = await client.Job.Query.Analysis.Static.Member.IntermediateForces
        .GetAsync(config =>
        {
            config.QueryParameters.Cases   = $"{ulsCase.Id}";
            config.QueryParameters.Members = $"{member.Id}";
        });

    var beamForces = ulsForces!.Results!.First();
    var maxMz = beamForces.Mz!.Max(v => Math.Abs(v ?? 0.0));
    Console.WriteLine($"Max ULS bending moment on Member {member.Id}: {maxMz:F2} kNm");

    // == Step 15 — Maximum SLS deflection ==========================
    var slsDisplacements = await client.Job.Query.Analysis.Static.Member.IntermediateDisplacements
        .GetAsync(config =>
        {
            config.QueryParameters.Cases   = $"{slsCase.Id}";
            config.QueryParameters.Members = $"{member.Id}";
        });

    var beamDisplacements = slsDisplacements!.Results!.First();
    var maxDeflection = beamDisplacements.TyGlobal!.Max(v => Math.Abs(v ?? 0.0));
    Console.WriteLine($"Max SLS deflection on Member {member.Id}: {maxDeflection * 1000:F2} mm");
    Console.WriteLine();

    // == Step 16 — Save and close ==================================
    Console.WriteLine($"Saving project to: {saveFilePath}");
    await client.Job.Save.PostAsync(new SaveJobRequest { FilePath = saveFilePath });
    Console.WriteLine("Project saved.");

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
