using SpaceGassApi;
using SpaceGassApi.Models;
using SpaceGassApi.Utils;


// ---------------------------------------------------------------
// Example: Steel Member DESIGN to AS 4100 (section selection)
//
// Builds the same simply-supported beam as Example.CreateSimpleBeam,
// but starts it on a deliberately heavy section, then lets a DESIGN
// run pick the lightest adequate section from the section library:
//   1.  Create the client and a new project
//   2.  Build the beam on a 610 UB 125
//   3.  Confirm which section library the design will select from
//   4.  Load cases, loads and a ULS combination
//   5.  Run a linear static analysis and wait for completion
//   6.  Create a steel member design group (optimise for weight)
//   7.  General design settings — groups and load cases
//   8.  Design iteration settings — re-analyse and iterate until stable
//   9.  Start the DESIGN run and poll until it finishes
//   10. Report what the run did and which section it chose
//   11. Query the check summary for the final section
//   12. Save and close
//
// With UpdateSections = true (the default) the run swaps the member's
// analysis section for the selected size and, as the iteration settings
// direct, re-runs the static analysis and the design until the analysis
// and design sections agree. See Example.SteelDesignCheck for a CHECK
// run that leaves the model unchanged.
//
// Prerequisites:
//   - SPACE GASS API running locally (default: http://localhost:34560)
//   - The "Aust300" section library installed (default in SPACE GASS)
//   - A licence for the AS 4100 steel member design module
// ---------------------------------------------------------------

// -- Configuration ------------------------------------------------
var saveFilePath = Path.Combine(
    Environment.GetFolderPath(Environment.SpecialFolder.Desktop),
    "SpaceGass Examples",
    "SteelDesignOptimise.sg");

const string designCode = SteelDesignExtensions.As4100;   // route segment: steel-design/{code}/...

var client = SpaceGassApiClient.CreateClient("http://localhost:34560");

try
{
    // == Step 1 — Create a new blank project =======================
    Console.WriteLine("Creating new blank project...");
    await client.Job.New.PostAsync();
    Console.WriteLine();

    // == Step 2 — Build the beam on a heavy section ================
    Console.WriteLine("Building a 6 m simply-supported beam on a 610 UB 125...");

    var node1 = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 0.0, Y = 0.0, Z = 0.0 });
    var node2 = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 6.0, Y = 0.0, Z = 0.0 });

    await client.Job.Structure.NodeRestraints.PostAsync(
        new NodeRestraintCreate { Node = node1!.Id, RestraintCode = "FFFFFF" });
    await client.Job.Structure.NodeRestraints.PostAsync(
        new NodeRestraintCreate { Node = node2!.Id, RestraintCode = "FFFRRR" });

    var steel = await client.Job.Structure.Materials.Library.PostAsync(
        new MaterialLibraryCreate { Library = "Aust", Name = "STEEL" });

    var initialSection = await client.Job.Structure.Sections.Library.PostAsync(
        new SectionLibraryCreate { Library = "Aust300", Name = "610 UB 125", Mark = "B1" });

    var member = await client.Job.Structure.Members.PostAsync(
        new MemberCreate
        {
            NodeA = node1.Id,
            NodeB = node2.Id,
            Section = initialSection!.Id,
            Material = steel!.Id,
        });
    Console.WriteLine($"  Member {member!.Id}: {initialSection.Name}");
    Console.WriteLine();

    // == Step 3 — Where the design selects sections from ===========
    // A DESIGN run picks replacement sections from the default section
    // library nominated in SPACE GASS (Preferences > Default Libraries),
    // narrowed by the design group's scan code to compatible shapes.
    var libraries = await client.Job.Settings.DefaultLibraries.GetAsync();
    Console.WriteLine($"Design will select sections from the \"{libraries!.Sections}\" library.");
    Console.WriteLine();

    // == Step 4 — Load cases, loads and a ULS combination ==========
    Console.WriteLine("Applying loads and defining the ULS combination...");

    var selfWeightCase = await client.Job.Loads.LoadCases.PostAsync(
        new LoadCaseCreate { Id = 1, Title = "Self-weight" });
    var deadCase = await client.Job.Loads.LoadCases.PostAsync(
        new LoadCaseCreate { Id = 2, Title = "Dead Load" });
    var liveCase = await client.Job.Loads.LoadCases.PostAsync(
        new LoadCaseCreate { Id = 3, Title = "Live Load" });

    await client.Job.Loads.SelfWeightLoads.PostAsync(
        new SelfWeightLoadCreate
        {
            LoadCase = selfWeightCase!.Id,
            AccelerationX = 0.0,
            AccelerationY = -1.0,    // 1 G downward
            AccelerationZ = 0.0,
        });

    await client.Job.Loads.MemberDistributedLoads.PostAsync(
        new MemberDistributedLoadCreate
        {
            LoadCase = deadCase!.Id,
            Member = member.Id,
            PositionUnits = LoadPositionUnits.Percent,
            StartPosition = 0.0,
            FinishPosition = 100.0,
            FyStart = -8.0,    // kN/m downward
            FyFinish = -8.0,
        });

    await client.Job.Loads.MemberDistributedLoads.PostAsync(
        new MemberDistributedLoadCreate
        {
            LoadCase = liveCase!.Id,
            Member = member.Id,
            PositionUnits = LoadPositionUnits.Percent,
            StartPosition = 0.0,
            FinishPosition = 100.0,
            FyStart = -10.0,
            FyFinish = -10.0,
        });

    // ULS: 1.2 G + 1.5 Q (AS/NZS 1170.0)
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
    Console.WriteLine($"  ULS case Id = {ulsCase!.Id}");
    Console.WriteLine();

    // == Step 5 — Run a linear static analysis =====================
    // The design run needs static results to start from. When it
    // re-analyses after swapping sections it uses the same stored
    // analysis settings, so the solver must be one the API supports.
    Console.WriteLine("Running linear static analysis...");
    await client.Job.Analysis.Static.Settings.PatchAsync(
        new StaticSettingsUpdate { SolverType = SolverType.Paradise });

    var analysisRun = await client.Job.Analysis.Static.RunLinear.PostAsync(
        new StaticSettingsUpdate());

    AnalysisRun finalAnalysis;
    while (true)
    {
        await Task.Delay(500);
        finalAnalysis = (await client.Job.Analysis.Runs[analysisRun!.RunId!.Value].GetAsync())!;
        if (finalAnalysis.Status is AnalysisRunStatus.Completed
                                 or AnalysisRunStatus.Failed
                                 or AnalysisRunStatus.Cancelled)
        {
            break;
        }
    }

    Console.WriteLine($"  Analysis {finalAnalysis.Status} in {finalAnalysis.ElapsedTime}");
    if (finalAnalysis.Status != AnalysisRunStatus.Completed)
    {
        throw new Exception($"Analysis did not complete: {finalAnalysis.ErrorMessage}");
    }
    Console.WriteLine();

    // == Step 6 — Create a steel member design group ===============
    Console.WriteLine("Creating steel member design group...");
    var group = await client.Job.Design.SteelMembers.PostAsync(
        new SteelMemberCreate
        {
            Id = 1,
            Description = "Floor beam B1",
            Members = member.Id!.Value.ToString(),
            MemberType = SteelMemberType.Beam,
            StrengthGrade = SteelStrengthGrade.Normal,
            LoadHeightPosition = LoadHeightPosition.Top,
            // Compression effective lengths as actual lengths (full span,
            // pinned ends) rather than from a buckling analysis.
            LengthUnitBasis = LengthUnitBasis.Actual,
            CalculateLcMajorFromBuckling = false,
            LcMajor = 6.0,
            CalculateLcMinorFromBuckling = false,
            LcMinor = 6.0,
            CalculateLbFromFlangeRestraints = true,
            // Pick the lightest adequate section rather than the shallowest.
            DesignCriteria = SteelDesignCriteria.Weight,
        });
    Console.WriteLine($"  Design group {group!.Id}: members {group.Members}, criteria {group.DesignCriteria}");
    Console.WriteLine();

    // == Step 7 — General design settings ==========================
    // Groups, LoadCases (and Sections, not used here) filter what the run
    // designs: which design groups, against which load cases, and — via
    // Sections — only members on those section property numbers.
    Console.WriteLine("Configuring general design settings...");
    var settings = await client.Job.Design.SteelDesign.Settings.PatchAsync(
        new SteelMemberDesignGeneralSettingsUpdate
        {
            Groups = new[] { group.Id!.Value }.ToFilterString(),
            LoadCases = new[] { ulsCase.Id!.Value }.ToFilterString(),
            LoadFactorLimit = 1.0,
        });
    Console.WriteLine($"  Groups: {settings!.Groups}, Load cases: {settings.LoadCases}");
    Console.WriteLine();

    // == Step 8 — Design iteration settings ========================
    // What happens after the run selects sections: re-run the static
    // analysis with the new sections, re-run the design, and keep
    // iterating (up to Iterations times) until the design settles.
    Console.WriteLine("Configuring design iteration settings...");
    var iteration = await client.Job.Design.SteelDesign.DesignIterationSettings.PatchAsync(
        new SteelMemberDesignIterationSettingsUpdate
        {
            RerunStaticAnalysis = true,
            RerunSteelMemberDesign = true,
            AutoIterate = true,
            Iterations = 5,
        });
    Console.WriteLine($"  Re-run static: {iteration!.RerunStaticAnalysis}, " +
                      $"auto-iterate: {iteration.AutoIterate}, max iterations: {iteration.Iterations}");
    Console.WriteLine();

    // == Step 9 — Start the DESIGN run and poll ====================
    // UpdateSections = true applies the selected sections to the model.
    // Everything in the body is optional — the settings PATCHed above
    // could equally have been passed here as per-run overrides.
    Console.WriteLine($"Starting {designCode} DESIGN run...");
    var designRun = await client.Job.Design.SteelDesign[designCode].RunDesign.PostAsync(
        new SteelDesignRunDesignRequest { UpdateSections = true });
    Console.WriteLine($"  Run {designRun!.RunId} {designRun.Status}; waiting for completion...");

    DesignRun finalDesign;
    while (true)
    {
        await Task.Delay(500);
        finalDesign = (await client.Job.Design.Runs[designRun.RunId!.Value].GetAsync())!;
        if (finalDesign.Status is AnalysisRunStatus.Completed
                               or AnalysisRunStatus.Failed
                               or AnalysisRunStatus.Cancelled)
        {
            break;
        }
    }

    Console.WriteLine($"  Design run {finalDesign.Status} in {finalDesign.ElapsedTime}");
    if (finalDesign.Status != AnalysisRunStatus.Completed)
    {
        throw new Exception($"Design run did not complete: {finalDesign.ErrorMessage}");
    }
    Console.WriteLine();

    // == Step 10 — What the run did ================================
    Console.WriteLine("Design run summary:");
    Console.WriteLine($"  Iterations:       {finalDesign.Iterations}");
    Console.WriteLine($"  Sections updated: {finalDesign.SectionsUpdated}");
    Console.WriteLine($"  Analysis re-run:  {finalDesign.AnalysisRerun}");
    Console.WriteLine($"  Members checked:  {finalDesign.MembersChecked}, failed: {finalDesign.MembersFailed}");
    foreach (var warning in finalDesign.Warnings ?? [])
    {
        Console.WriteLine($"  Warning: {warning}");
    }

    // Re-read the member to see which section the design chose.
    var designedMember = await client.Job.Structure.Members[member.Id!.Value].GetAsync();
    var designedSection = await client.Job.Structure.Sections[designedMember!.Section!.Value].GetAsync();
    Console.WriteLine($"  Section: {initialSection.Name}  ->  {designedSection!.Name}");
    Console.WriteLine();

    // == Step 11 — Check summary for the final section =============
    Console.WriteLine("Steel member check summary:");
    var summary = await client.Job.Query.Design.SteelMember.CheckSummary.GetAsync(
        config => config.QueryParameters.Members = new[] { member.Id!.Value }.ToFilterString());

    foreach (var row in summary!.Results ?? [])
    {
        Console.WriteLine($"  Member {row.Member}: {row.Section}");
        Console.WriteLine($"    Load factor:   {row.LoadFactor:F3}  (flag: {row.Flag})");
        Console.WriteLine($"    Critical case: {row.CriticalCase}");
        Console.WriteLine($"    Failure mode:  {row.Failure}");
    }
    Console.WriteLine();

    // == Step 12 — Save and close ==================================
    Console.WriteLine($"Saving model to: {saveFilePath}");
    await client.Job.Save.PostAsync(new SaveJobRequest { FilePath = saveFilePath });
    Console.WriteLine("Project saved.");
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
    // Always close the active job so the next run starts clean.
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
