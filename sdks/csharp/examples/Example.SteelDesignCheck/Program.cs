using SpaceGassApi;
using SpaceGassApi.Models;
using SpaceGassApi.Utils;


// ---------------------------------------------------------------
// Example: Steel Member Design CHECK to AS 4100
//
// Builds the same simply-supported beam as Example.CreateSimpleBeam,
// analyses it, then verifies the beam's section against AS 4100:
//   1.  Create the client and a new project
//   2.  Build the beam (nodes, restraints, material, section, member)
//   3.  Load cases, loads and a ULS combination
//   4.  Run a linear static analysis and wait for completion
//   5.  List the design codes this seat can check to
//   6.  Create a steel member design group for the beam
//   7.  Configure the general design settings (which groups / cases)
//   8.  Configure the AS 4100 code-specific settings
//   9.  Start a design CHECK run and poll until it finishes
//   10. Query the per-member check summary (load factor, critical case)
//   11. Save and close
//
// A CHECK run verifies the members' current sections without changing
// the model. See Example.SteelDesignOptimise for a DESIGN run that
// selects new sections.
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
    "SteelDesignCheck.sg");

const string designCode = SteelDesignExtensions.As4100;   // route segment: steel-design/{code}/...

var client = SpaceGassApiClient.CreateClient("http://localhost:34560");

try
{
    // == Step 1 — Create a new blank project =======================
    Console.WriteLine("Creating new blank project...");
    await client.Job.New.PostAsync();
    Console.WriteLine();

    // == Step 2 — Build the beam ===================================
    Console.WriteLine("Building a 6 m simply-supported beam...");

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

    var section = await client.Job.Structure.Sections.Library.PostAsync(
        new SectionLibraryCreate { Library = "Aust300", Name = "360 UB 44.7", Mark = "B1" });

    var member = await client.Job.Structure.Members.PostAsync(
        new MemberCreate
        {
            NodeA = node1.Id,
            NodeB = node2.Id,
            Section = section!.Id,
            Material = steel!.Id,
        });
    Console.WriteLine($"  Member {member!.Id}: {section.Name} ({steel.Name})");
    Console.WriteLine();

    // == Step 3 — Load cases, loads and a ULS combination ==========
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

    // == Step 4 — Run a linear static analysis =====================
    // A design run needs static analysis results for the design load
    // cases, so analyse first.
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

    // == Step 5 — List the available design codes ==================
    // Does not need an open job. Each entry says whether this seat is
    // licensed for the code and which edition a run is completed under.
    Console.WriteLine("Steel member design codes:");
    var codes = await client.Job.Design.SteelDesign.Codes.GetAsync();
    foreach (var c in codes!)
    {
        Console.WriteLine($"  {c.Code,-8} {c.Edition,-16} licensed: {c.IsLicensed}");
    }

    var as4100 = codes.FirstOrDefault(c => c.Code == SteelDesignCode.As4100);
    if (as4100?.IsLicensed != true)
    {
        throw new Exception("This seat is not licensed for AS 4100 steel member design.");
    }
    Console.WriteLine();

    // == Step 6 — Create a steel member design group ===============
    // A design group (SPACE GASS "Design - Steel Members") spans one or
    // more analytical members. Members is a plain comma-separated list
    // of member Ids (ranges are not supported here).
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
            // Compression effective lengths: by default these come from a
            // buckling analysis, which this model hasn't run. Give them
            // explicitly as actual lengths (the full 6 m span, pinned ends).
            LengthUnitBasis = LengthUnitBasis.Actual,
            CalculateLcMajorFromBuckling = false,
            LcMajor = 6.0,
            CalculateLcMinorFromBuckling = false,
            LcMinor = 6.0,
            // Work out the lateral-torsional buckling length from the
            // flange restraints (the ends are restrained by default).
            CalculateLbFromFlangeRestraints = true,
        });
    Console.WriteLine($"  Design group {group!.Id}: members {group.Members}");
    Console.WriteLine();

    // == Step 7 — General design settings ==========================
    // Code-independent settings shared by every design code: which
    // groups and load cases to design/check, section availability, etc.
    // Settings are saved with the job.
    Console.WriteLine("Configuring general design settings...");
    var settings = await client.Job.Design.SteelDesign.Settings.PatchAsync(
        new SteelMemberDesignGeneralSettingsUpdate
        {
            Groups = new[] { group.Id!.Value }.ToFilterString(),
            LoadCases = new[] { ulsCase.Id!.Value }.ToFilterString(),
            Stations = 10,            // intermediate stations checked along each member
            LoadFactorLimit = 1.0,
        });
    Console.WriteLine($"  Groups: {settings!.Groups}, Load cases: {settings.LoadCases}, Stations: {settings.Stations}");
    Console.WriteLine();

    // == Step 8 — AS 4100 code-specific settings ===================
    // Each design code has its own settings object (AS 4100 and NZS 3404
    // differ). They can be PATCHed at steel-design/{code}/settings, or —
    // as here — passed as a per-run override on the run request; either
    // way they are stored with the job. The SDK's SteelDesignExtensions
    // let you assign the code's own settings object straight to
    // CodeSettings; the Code discriminator is filled in for you.
    Console.WriteLine("Preparing AS 4100 settings...");
    var as4100Settings = new SteelMemberDesignSettingsAS4100Update
    {
        SlendernessRatioCheck = true,
        UseKtFactorForTension = true,
    };
    Console.WriteLine("  Slenderness ratio check on, Kt factor for tension on");
    Console.WriteLine();

    // == Step 9 — Start the CHECK run and poll =====================
    // The body is optional; settings supplied here are written to the
    // job's stored settings before the run starts. Analysis and design
    // runs share one queue, so QueuePosition may be > 1.
    Console.WriteLine($"Starting {designCode} design CHECK run...");
    var designRun = await client.Job.Design.SteelDesign[designCode].RunCheck.PostAsync(
        new SteelDesignRunCheckRequest { CodeSettings = as4100Settings });
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

    // Once Completed the run carries its result summary.
    Console.WriteLine($"  Mode: {finalDesign.Mode}, code: {finalDesign.Code}");
    Console.WriteLine($"  Members checked: {finalDesign.MembersChecked}, failed: {finalDesign.MembersFailed}");
    foreach (var warning in finalDesign.Warnings ?? [])
    {
        Console.WriteLine($"  Warning: {warning}");
    }
    Console.WriteLine();

    // == Step 10 — Query the check summary =========================
    // One row per member. LoadFactor is the capacity ratio the member
    // achieved; the Flag and Failure fields describe the governing
    // check, and CriticalCase is the load case that governed.
    Console.WriteLine("Steel member check summary:");
    var summary = await client.Job.Query.Design.SteelMember.CheckSummary.GetAsync(
        config => config.QueryParameters.Members = new[] { member.Id!.Value }.ToFilterString());

    foreach (var row in summary!.Results ?? [])
    {
        Console.WriteLine($"  Member {row.Member}: {row.Section}");
        Console.WriteLine($"    Load factor:   {row.LoadFactor:F3}  (flag: {row.Flag})");
        Console.WriteLine($"    Critical case: {row.CriticalCase}");
        Console.WriteLine($"    Failure mode:  {row.Failure}");
        Console.WriteLine($"    Yield stress:  {row.Yield}  Segment length: {row.SegmentLength}");
    }
    Console.WriteLine();

    // == Step 11 — Save and close ==================================
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
