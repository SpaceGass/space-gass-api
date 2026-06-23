using SpaceGassApi;
using SpaceGassApi.Models;
using SpaceGassApi.Utils;


// Bridge grillage with a T44 moving load.
//
// Builds a 3-span, 2-lane grillage and runs an AS 5100 T44 moving-load
// analysis — demonstrating the moving-load API (vehicle import, travel paths,
// scenario, generation). The girder + concrete deck sections and their
// materials can't be created via the API yet, so they come from
// GrillageTemplate.sgbase (shipped next to this example); everything else is
// built here.
//
// Prerequisites:
//   - SPACE GASS API running locally (default http://localhost:34560)
//   - The "Australia" vehicle library installed (for T44)
//   - GrillageTemplate.sgbase next to the exe (copied by the .csproj)

var templatePath = Path.Combine(AppContext.BaseDirectory, "GrillageTemplate.sgbase");

var saveFilePath = Path.Combine(
    Environment.GetFolderPath(Environment.SpecialFolder.Desktop),
    "SpaceGass Examples",
    "GrillageMovingLoad.sg");

// Section + material Ids defined in the template.
const int girderSectionId = 1;          // Bridge Girder (steel WB)
const int interiorStripSectionId = 2;   // 1.0 m concrete deck strip
const int endStripSectionId = 3;        // 0.5 m concrete deck strip (end lines)
const int steelMaterialId = 1;
const int concreteMaterialId = 2;

// Geometry. X = along the bridge, Z = across, Y = up.
double[] spanLengths = { 20.0, 20.0, 20.0 };          // 3 spans, 60 m total
double[] girderZ = { 0.0, 1.75, 3.5, 5.25, 7.0 };     // 5 girders, 1.75 m c/c
double stripSpacing = 1.0;                            // transverse strips @ 1 m
int[] lanePathGirderIndices = { 1, 3 };               // girders 2 & 4 = lane centrelines
double wearingSurfacePressure = 2.0;                  // SDL, kN/m^2

int numGirders = girderZ.Length;
double totalLength = spanLengths.Sum();
int numStations = (int)Math.Round(totalLength / stripSpacing) + 1;
int numBays = numGirders - 1;

var supportXs = new List<double> { 0.0 };
double running = 0.0;
foreach (var span in spanLengths) { running += span; supportXs.Add(running); }
var supportStations = supportXs.Select(x => (int)Math.Round(x / stripSpacing)).ToHashSet();

// Deterministic Ids so the grid wires up without round-tripping.
double StationX(int i) => i * stripSpacing;
int NodeId(int g, int i) => g * numStations + i + 1;
int GirderMemberId(int g, int i) => g * (numStations - 1) + i + 1;
int StripMemberId(int i, int b) => numGirders * (numStations - 1) + i * numBays + b + 1;
int totalMembers = numGirders * (numStations - 1) + numStations * numBays;

var client = SpaceGassApiClient.CreateClient("http://localhost:34560");

try
{
    // New job from the template (fresh, unsaved — the template file is untouched).
    if (!File.Exists(templatePath))
        throw new FileNotFoundException(
            $"Template not found: {templatePath} (the .csproj should copy it next to the exe).");

    Console.WriteLine($"Uploading template: {Path.GetFileName(templatePath)}");
    await client.Job.NewFromTemplate.PostAsync(new NewFromTemplateRequest(templatePath));
    Console.WriteLine("New job created from template (unsaved).");
    Console.WriteLine();

    // Show what the template provides, then validate the Ids we rely on.
    var sections = await client.Job.Structure.Sections.GetAsync() ?? new();
    var materials = await client.Job.Structure.Materials.GetAsync() ?? new();
    var primaryCases = await client.Job.Loads.LoadCases.GetAsync() ?? new();

    Console.WriteLine("Template sections:");
    foreach (var s in sections)
        Console.WriteLine($"  [{s.Id}] {s.Name}  (mark: {s.Mark}, A={s.A}, Iz={s.Iz})");
    Console.WriteLine("Template materials:");
    foreach (var m in materials)
        Console.WriteLine($"  [{m.Id}] {m.Name}  (E={m.YoungsModulus})");
    Console.WriteLine("Template primary load cases:");
    foreach (var lc in primaryCases)
        Console.WriteLine($"  [{lc.Id}] {lc.Title}");
    Console.WriteLine();

    foreach (var (id, what) in new[]
    {
        (girderSectionId, "girder section"),
        (interiorStripSectionId, "1 m deck-strip section"),
        (endStripSectionId, "0.5 m deck-strip section"),
    })
    {
        if (sections.All(s => s.Id != id))
            throw new Exception(
                $"Template is missing the expected {what} (Id {id}). " +
                $"Sections found: [{string.Join(", ", sections.Select(s => s.Id))}].");
    }
    foreach (var (id, what) in new[] { (steelMaterialId, "STEEL"), (concreteMaterialId, "Concrete") })
    {
        if (materials.All(m => m.Id != id))
            throw new Exception($"Template is missing the expected {what} material (Id {id}).");
    }
    if (primaryCases.Count == 0)
        throw new Exception("The template defines no load cases — expected a self-weight case.");

    var selfWeightCase = primaryCases[0];   // pre-baked self-weight case
    Console.WriteLine($"Using self-weight case [{selfWeightCase.Id}] '{selfWeightCase.Title}'.");
    Console.WriteLine();

    // Nodes — a grid of girders x stations.
    Console.WriteLine($"Creating {numGirders * numStations} nodes ({numGirders} girders x {numStations} stations)...");
    var nodes = new List<NodeCreate>();
    for (int g = 0; g < numGirders; g++)
        for (int i = 0; i < numStations; i++)
            nodes.Add(new NodeCreate { Id = NodeId(g, i), X = StationX(i), Y = 0.0, Z = girderZ[g] });

    var nodeResult = await client.Job.Structure.Nodes.Bulk.PostAsync(nodes);
    if (nodeResult?.Errors is { Count: > 0 } nodeErrors)
        throw new Exception($"Node bulk create reported {nodeErrors.Count} error(s); first: {nodeErrors[0].Error}");
    Console.WriteLine($"  {nodes.Count} nodes created.");
    Console.WriteLine();

    // Members — longitudinal girders, plus transverse deck strips (the end
    // lines use the 0.5 m strip, interior lines the 1 m strip).
    Console.WriteLine($"Creating {totalMembers} members (girders + deck strips)...");
    var members = new List<MemberCreate>();

    for (int g = 0; g < numGirders; g++)
        for (int i = 0; i < numStations - 1; i++)
            members.Add(new MemberCreate
            {
                Id = GirderMemberId(g, i),
                NodeA = NodeId(g, i),
                NodeB = NodeId(g, i + 1),
                Section = girderSectionId,
                Material = steelMaterialId,
            });

    for (int i = 0; i < numStations; i++)
    {
        bool isEndLine = i == 0 || i == numStations - 1;
        for (int b = 0; b < numBays; b++)
            members.Add(new MemberCreate
            {
                Id = StripMemberId(i, b),
                NodeA = NodeId(b, i),
                NodeB = NodeId(b + 1, i),
                Section = isEndLine ? endStripSectionId : interiorStripSectionId,
                Material = concreteMaterialId,
            });
    }

    var memberResult = await client.Job.Structure.Members.Bulk.PostAsync(members);
    if (memberResult?.Errors is { Count: > 0 } memberErrors)
        throw new Exception($"Member bulk create reported {memberErrors.Count} error(s); first: {memberErrors[0].Error}");
    Console.WriteLine($"  {members.Count} members created.");
    Console.WriteLine();

    // Bearings. Restraint code is TX TY TZ RX RY RZ (F = fixed, R = released):
    // abutment 1 is fixed; the piers and abutment 2 are guided longitudinally.
    Console.WriteLine("Restraining bearing lines...");
    var supportNodeIds = new List<int>();
    bool firstSupport = true;
    foreach (var station in supportStations.OrderBy(s => s))
    {
        var code = firstSupport ? "FFFRRR" : "RFFRRR";
        for (int g = 0; g < numGirders; g++)
        {
            var nodeId = NodeId(g, station);
            await client.Job.Structure.NodeRestraints.PostAsync(
                new NodeRestraintCreate { Node = nodeId, RestraintCode = code });
            supportNodeIds.Add(nodeId);
        }
        firstSupport = false;
    }
    Console.WriteLine($"  {supportNodeIds.Count} support nodes restrained.");
    Console.WriteLine();

    // Superimposed dead load (wearing surface) as a UDL on each deck strip;
    // the end strips carry half the longitudinal tributary width.
    Console.WriteLine($"Applying {wearingSurfacePressure} kN/m^2 SDL to the deck strips...");
    var sdlCase = await client.Job.Loads.LoadCases.PostAsync(
        new LoadCaseCreate { Id = 2, Title = "G2 - Superimposed Dead Load (wearing surface)" });

    var sdlLoads = new List<MemberDistributedLoadCreate>();
    for (int i = 0; i < numStations; i++)
    {
        double tributaryX = (i == 0 || i == numStations - 1) ? stripSpacing / 2.0 : stripSpacing;
        double udl = -wearingSurfacePressure * tributaryX;   // kN/m, downward
        for (int b = 0; b < numBays; b++)
            sdlLoads.Add(new MemberDistributedLoadCreate
            {
                LoadCase = sdlCase!.Id,
                Member = StripMemberId(i, b),
                PositionUnits = LoadPositionUnits.Percent,
                StartPosition = 0.0,
                FinishPosition = 100.0,
                FyStart = udl,
                FyFinish = udl,
            });
    }
    await client.Job.Loads.MemberDistributedLoads.Bulk.PostAsync(sdlLoads);
    Console.WriteLine($"  SDL applied to {sdlLoads.Count} deck strips (case {sdlCase!.Id}).");
    Console.WriteLine();

    // Total dead load = self-weight + SDL. A scenario can combine with only
    // one load case, so roll the permanent loads into a single combination.
    var totalDeadLoad = await client.Job.Loads.CombinationLoadCases.PostAsync(
        new CombinationLoadCaseCreate
        {
            Id = 50,
            Title = "Total Dead Load (self-weight + SDL)",
            CombinationItems = new List<CombinationLoadCaseItem>
            {
                new() { LoadCase = selfWeightCase.Id, MultiplyingFactor = 1.0 },
                new() { LoadCase = sdlCase.Id,        MultiplyingFactor = 1.0 },
            },
        });
    Console.WriteLine($"Total Dead Load combination = case {totalDeadLoad!.Id}.");
    Console.WriteLine();

    // --- T44 moving load ---
    Console.WriteLine("Setting up the T44 moving load...");

    await client.Job.Loads.MovingLoads.Settings.PatchAsync(
        new MovingLoadSettingsUpdate
        {
            ApplyToClosestMember = true,
            CheckVerticalProximity = false,
            KeepLoadsWithinTravelPath = false,
        });

    // Import T44 from the vehicle library and print its wheel layout.
    var t44 = await client.Job.Loads.MovingLoads.Vehicles.Library.PostAsync(
        new MovingLoadVehicleLibraryCreate { Name = "T44-3", Library = "Australia" });
    Console.WriteLine($"  Imported vehicle [{t44!.Id}] {t44.Name} from {t44.Library}.");

    var wheels = t44.Loads ?? new();
    var loadUnits = t44.LoadUnits;
    if (wheels.Count == 0)
    {
        var full = await client.Job.Loads.MovingLoads.Vehicles[t44.Id!.Value].GetAsync();
        wheels = full?.Loads ?? wheels;
        loadUnits = full?.LoadUnits ?? loadUnits;
    }

    if (wheels.Count == 0)
    {
        Console.WriteLine("  (vehicle returned no wheel loads — check the library item name).");
    }
    else
    {
        Console.WriteLine(
            $"  T44 wheel loads — {wheels.Count} wheels " +
            $"(units: length={loadUnits?.Length}, force={loadUnits?.Force}):");
        Console.WriteLine("        #         X         Y        Fx        Fy        Fz");
        int w = 1;
        foreach (var wheel in wheels)
            Console.WriteLine(
                $"      {w++,3}  {wheel.X ?? 0,8:F3}  {wheel.Y ?? 0,8:F3}  " +
                $"{wheel.Fx ?? 0,8:F2}  {wheel.Fy ?? 0,8:F2}  {wheel.Fz ?? 0,8:F2}");

        // Truck footprint: longitudinal axle base and transverse wheel track.
        double axleBase = wheels.Max(k => k.X ?? 0) - wheels.Min(k => k.X ?? 0);
        double trackWidth = wheels.Max(k => k.Y ?? 0) - wheels.Min(k => k.Y ?? 0);
        double sumFy = wheels.Sum(k => k.Fy ?? 0);
        double sumFz = wheels.Sum(k => k.Fz ?? 0);
        Console.WriteLine(
            $"      Footprint: axle base (X)={axleBase:F3}, track width (Y)={trackWidth:F3} {loadUnits?.Length}; " +
            $"total Fy={sumFy:F1}, Fz={sumFz:F1} {loadUnits?.Force}");
    }

    // One travel path per lane, centred on girders 2 and 4 (NodeKey = 0 means
    // the X/Y/Z are absolute coordinates).
    var travelPathIds = new List<int>();
    for (int k = 0; k < lanePathGirderIndices.Length; k++)
    {
        int gi = lanePathGirderIndices[k];
        double laneZ = girderZ[gi];
        var path = await client.Job.Loads.MovingLoads.TravelPaths.PostAsync(
            new MovingLoadTravelPathCreate { Name = $"Lane {k + 1} (girder {gi + 1})" });

        await client.Job.Loads.MovingLoads.TravelPaths[path!.Id!.Value].Stations.PutAsync(
            new List<MovingLoadStation>
            {
                new() { NodeKey = 0, X = 0.0,         Y = 0.0, Z = laneZ, Radius = 0.0 },
                new() { NodeKey = 0, X = totalLength, Y = 0.0, Z = laneZ, Radius = 0.0 },
            });
        travelPathIds.Add(path.Id.Value);
        Console.WriteLine($"  Travel path [{path.Id}] '{path.Name}' along Z = {laneZ} m.");
    }

    // Scenario: a T44 on each lane, combined with the Total Dead Load
    // (1.2 G + 1.5 live, 1.3 dynamic load allowance).
    var scenario = await client.Job.Loads.MovingLoads.Scenarios.PostAsync(
        new MovingLoadScenarioCreate
        {
            Name = "T44 - both lanes",
            Include = true,
            StartingLoadCase = 101,
            TimeInterval = 0.5,
            Loads = new List<MovingLoadScenarioLoad>
            {
                new()
                {
                    LoadType = MovingLoadType.Vehicle,
                    VehicleId = t44.Id,
                    TravelPathId = travelPathIds[0],
                    Speed = 10.0,
                    StartPosition = 0.0,
                    LoadFactor = 1.0,
                    LaneFactor = 1.0,      // AS 5100 lane modification factor
                    DynamicFactor = 1.3,   // T44 dynamic load allowance (~0.3)
                    GenerateStationaryLc = MovingLoadStationaryOption.StartingLoadCase,
                },
                new()
                {
                    LoadType = MovingLoadType.Vehicle,
                    VehicleId = t44.Id,
                    TravelPathId = travelPathIds[1],
                    Speed = 10.0,
                    StartPosition = 0.0,
                    LoadFactor = 1.0,
                    LaneFactor = 1.0,
                    DynamicFactor = 1.3,
                    GenerateStationaryLc = MovingLoadStationaryOption.StartingLoadCase,
                },
            },
            Combinations = new List<MovingLoadCombination>
            {
                new()
                {
                    ScenarioFactor = 1.5,
                    CombineLoadCase = totalDeadLoad.Id,
                    LoadCaseFactor = 1.2,
                    StartingCombinationCase = 201,
                },
            },
        });
    Console.WriteLine($"  Scenario [{scenario!.Id}] '{scenario.Name}' created.");

    // Select the elements the loads apply to (the whole grillage). This MUST
    // come after the scenario block — the vehicle/path/scenario setup resets
    // the selection, so an earlier call is silently cleared by generation time.
    var elements = await client.Job.Loads.MovingLoads.ElementsToLoad.PatchAsync(
        new MovingLoadElementsUpdate { Members = Enumerable.Range(1, totalMembers).ToFilterString() });
    Console.WriteLine($"  Elements to load: members='{elements?.Members}'.");

    var generation = await client.Job.Loads.MovingLoads.Generate.PostAsync(
        new MovingLoadGenerateRequest());
    var movingCaseIds = (generation!.GeneratedLoadCaseIds ?? new())
        .Where(id => id.HasValue).Select(id => id!.Value).ToArray();
    Console.WriteLine($"  Generated {movingCaseIds.Length} moving load case(s).");
    Console.WriteLine();

    // A named filter per member type (selectable in the SPACE GASS UI).
    Console.WriteLine("Creating selection filters...");
    await client.Job.Filters.PostAsync(new FilterCreate
    {
        Name = "Girders (WB)",
        Sections = new FilterSectionsUpdate
        {
            IsActive = true,
            Mode = FilterMode.Include,
            Sections = girderSectionId.ToString(),
        },
    });

    await client.Job.Filters.PostAsync(new FilterCreate
    {
        Name = "Deck slab strips",
        Sections = new FilterSectionsUpdate
        {
            IsActive = true,
            Mode = FilterMode.Include,
            Sections = $"{interiorStripSectionId},{endStripSectionId}",
        },
    });

    await client.Job.Filters.PostAsync(new FilterCreate
    {
        Name = "Bridge supports",
        Nodes = new FilterNodesUpdate
        {
            IsActive = true,
            Mode = FilterMode.Include,
            Nodes = supportNodeIds.ToArray().ToFilterString(),
        },
    });
    Console.WriteLine("  Filters: 'Girders (WB)', 'Deck slab strips', 'Bridge supports'.");
    Console.WriteLine();

    Console.WriteLine($"Saving model to: {saveFilePath}");
    await client.Job.Save.PostAsync(new SaveJobRequest { FilePath = saveFilePath });
    Console.WriteLine();

    // Analyse, then report the peak girder moment from the T44 envelope.
    var run = await client.Job.Analysis.Static.RunLinear.PostAsync(new StaticSettingsUpdate());
    Console.WriteLine($"Run {run!.RunId} queued; waiting for completion...");

    AnalysisRun finalRun;
    while (true)
    {
        await Task.Delay(500);
        finalRun = (await client.Job.Analysis.Runs[run.RunId!.Value].GetAsync())!;
        if (finalRun.Status is AnalysisRunStatus.Completed
                            or AnalysisRunStatus.Failed
                            or AnalysisRunStatus.Cancelled)
            break;
    }
    Console.WriteLine($"  Analysis {finalRun.Status} in {finalRun.ElapsedTime}");
    if (finalRun.Status != AnalysisRunStatus.Completed)
        throw new Exception($"Analysis did not complete: {finalRun.ErrorMessage}");
    Console.WriteLine();

    if (movingCaseIds.Length == 0)
    {
        Console.WriteLine("No moving load cases were generated — skipping the result query.");
    }
    else
    {
        // Worst bending moment on the central girder across the moving snapshots.
        int centreGirder = numGirders / 2;
        var centreMembers = Enumerable.Range(0, numStations - 1)
            .Select(i => GirderMemberId(centreGirder, i)).ToArray();

        var forces = await client.Job.Query.Analysis.Static.MemberIntermediateForces.GetAsync(
            config =>
            {
                config.QueryParameters.LoadCases = movingCaseIds.ToFilterString();
                config.QueryParameters.Members = centreMembers.ToFilterString();
            });

        double peakMz = 0.0;
        int? peakCase = null, peakMember = null;
        foreach (var row in forces?.Results ?? new())
        {
            foreach (var mz in row.Mz ?? new())
            {
                double v = Math.Abs(mz ?? 0.0);
                if (v > peakMz) { peakMz = v; peakCase = row.LoadCase; peakMember = row.Member; }
            }
        }

        Console.WriteLine(
            $"Peak |Mz| on central girder (line {centreGirder + 1}): {peakMz:F1} kNm " +
            $"(member {peakMember}, moving load case {peakCase}).");
    }
    Console.WriteLine();

    Console.WriteLine($"Saving analysed model to: {saveFilePath}");
    await client.Job.Save.PostAsync(new SaveJobRequest { FilePath = saveFilePath });
    Console.WriteLine("Done.");
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
