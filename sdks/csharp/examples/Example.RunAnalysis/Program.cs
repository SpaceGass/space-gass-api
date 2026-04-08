using SpaceGassApi;
using SpaceGassApi.Models;


// ---------------------------------------------------------------
// Example: Run a Linear Static Analysis
//
// Demonstrates how to:
//   1. Open an existing SPACE GASS project
//   2. Start a linear static analysis run
//   3. Poll for progress until completion
//   4. Display results summary
//   5. Query node reactions from the completed analysis
//
// Prerequisites:
//   - SPACE GASS API running locally (default: https://localhost:53483)
//   - A valid API key
//   - An existing .sg project file with structure and loads defined
// ---------------------------------------------------------------

// -- Configuration ------------------------------------------------
// Path to an existing SPACE GASS project file with structure and loads.
// Change this to point to your own project file.
var projectFilePath = Path.Combine(
    Environment.GetFolderPath(Environment.SpecialFolder.Desktop),
    "SpaceGass Examples",
    "MyProject.sg");

var pollIntervalMs = 500; // How often to poll for progress (milliseconds)

var client = SpaceGassApiClient.CreateClient();

try
{
    // -- Open the project ------------------------------------------
    Console.WriteLine($"Opening project: {projectFilePath}");
    await client.Job.Open.PostAsync(new OpenJobRequest { FilePath = projectFilePath });
    Console.WriteLine("Project opened.");
    Console.WriteLine();

    // -- Start a linear static analysis ----------------------------
    // The body uses PATCH semantics — only non-null fields override
    // the current job settings. Pass an empty object to run with
    // current settings as-is.
    Console.WriteLine("Starting linear static analysis...");
    var run = await client.Job.Analysis.Static.RunLinear.PostAsync(new StaticSettingsUpdate());

    if (run == null)
    {
        Console.Error.WriteLine("Error: No response from run-linear endpoint.");
        return 1;
    }

    Console.WriteLine($"  Run ID:  {run.RunId}");
    Console.WriteLine($"  Status:  {run.Status}");
    Console.WriteLine();

    // -- Poll for progress until completion ------------------------
    Console.WriteLine("Polling for progress...");
    Console.WriteLine();

    var lastStep = -1;
    var runId = run.RunId!.Value;

    while (true)
    {
        await Task.Delay(pollIntervalMs);

        var status = await client.Job.Analysis.Runs[runId].GetAsync();
        if (status == null) break;

        // Print progress updates
        if (status.Progress != null)
        {
            var p = status.Progress;
            var stepInfo = $"Step {p.CurrentStep}/{p.TotalSteps}";
            var pctInfo = $"{p.IterationPercentage}%";
            var statusText = p.StatusText ?? "";
            var loadCase = p.LoadCaseStatus != null ? $" | Load cases: {p.LoadCaseStatus}" : "";

            // Print step label when it changes
            if (p.CurrentStep != lastStep && p.StepLabels != null)
            {
                var stepIndex = p.CurrentStep ?? 0;
                if (stepIndex < p.StepLabels.Count)
                {
                    var label = p.StepLabels[stepIndex];
                    if (!string.IsNullOrEmpty(label))
                    {
                        Console.WriteLine($"  [{stepInfo}] {label}");
                    }
                }
                lastStep = p.CurrentStep ?? -1;
            }

            Console.Write($"\r  {stepInfo} | {pctInfo}{loadCase} | {statusText}".PadRight(80));
        }
        else if (status.ElapsedTime != null)
        {
            Console.Write($"\r  Status: {status.Status} | Elapsed: {status.ElapsedTime}".PadRight(80));
        }

        // Check for terminal states
        if (status.Status == AnalysisRunStatus.Completed ||
            status.Status == AnalysisRunStatus.Failed ||
            status.Status == AnalysisRunStatus.Cancelled)
        {
            Console.WriteLine();
            Console.WriteLine();

            // -- Display result summary --------------------------------
            Console.WriteLine($"Analysis {status.Status}!");
            Console.WriteLine($"  Elapsed time: {status.ElapsedTime}");

            if (status.Header != null)
                Console.WriteLine($"  Header: {status.Header}");

            // Show parameters
            if (status.Parameters?.AdditionalData != null)
            {
                Console.WriteLine("  Parameters:");
                foreach (var kvp in status.Parameters.AdditionalData)
                {
                    Console.WriteLine($"    {kvp.Key} {kvp.Value}");
                }
            }

            // Show convergence history (non-linear only)
            if (status.ConvergenceHistory != null && status.ConvergenceHistory.Count > 0)
            {
                Console.WriteLine("  Convergence history:");
                foreach (var entry in status.ConvergenceHistory)
                {
                    Console.WriteLine($"    Iteration {entry.Iteration}: {entry.Percentage}%");
                }
            }

            // Show warnings
            if (status.Warnings != null && status.Warnings.Count > 0)
            {
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine($"  Warnings ({status.Warnings.Count}):");
                foreach (var warning in status.Warnings)
                {
                    Console.WriteLine($"    {warning}");
                }
                Console.ResetColor();
            }

            // Show error
            if (status.ErrorMessage != null)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"  Error: {status.ErrorMessage}");
                Console.ResetColor();
            }

            break;
        }
    }

    // -- Query results (only if completed) -------------------------
    Console.WriteLine();
    Console.WriteLine("Querying node reactions...");

    var queryResult = await client.Job.Query.Analysis.Static.Node.Reactions.GetAsync();
    var reactions = queryResult?.Results;
    if (reactions != null && reactions.Count > 0)
    {
        Console.WriteLine($"  Found {reactions.Count} reaction result(s).");
        // Print first few reactions as a sample
        foreach (var r in reactions.Take(3))
        {
            Console.WriteLine($"    Node {r.Node}, LC {r.Case}: " +
                $"FX={r.Fx:F2}, FY={r.Fy:F2}, FZ={r.Fz:F2}");
        }
        if (reactions.Count > 3)
            Console.WriteLine($"    ... and {reactions.Count - 3} more.");
    }
    else
    {
        Console.WriteLine("  No reactions found.");
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
