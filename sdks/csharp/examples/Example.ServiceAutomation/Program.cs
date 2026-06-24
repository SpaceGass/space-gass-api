using System.Diagnostics;
using SpaceGassApi;


// ---------------------------------------------------------------
// Example: Service Automation
//
// Mirrors the Service Automation guide in the Zudoku docs site.
// Demonstrates the four-step service lifecycle:
//
//   1. Probe  — try Service.Info to see if the service is already running
//   2. Start  — if not, launch SpaceGassApi.exe as a child process
//   3. Wait   — poll Service.Info until it responds (or fail with a timeout)
//   4. Stop   — terminate the child process when done, but only if we
//               started it ourselves
//
// Update SERVICE_EXE_PATH below to match your SPACE GASS installation.
//
// Prerequisites:
//   - SPACE GASS installed locally
//   - SPACE GASS has been opened at least once to initialise data files
// ---------------------------------------------------------------

const string ServiceExePath = @"C:\Program Files\SPACE GASS 14.5\SpaceGassApi.exe";

var client = SpaceGassApiClient.CreateClient("http://localhost:34560");
Process? serviceProcess = null;

// Hook Ctrl+C so the service still shuts down on a hard interrupt
Console.CancelKeyPress += (_, _) =>
{
    if (serviceProcess is not null && !serviceProcess.HasExited)
    {
        Console.WriteLine("\nCtrl+C received — stopping the service...");
        serviceProcess.Kill(entireProcessTree: true);
    }
};

try
{
    // == Step 1 — Probe ============================================
    if (await IsServiceReadyAsync(client))
    {
        Console.WriteLine("Service was already running — reusing it.");
    }
    else
    {
        // == Step 2 — Start ========================================
        Console.WriteLine($"Starting the SPACE GASS API service: {ServiceExePath}");
        serviceProcess = Process.Start(new ProcessStartInfo
        {
            FileName = ServiceExePath,
            UseShellExecute = false,
            CreateNoWindow = true,
        });

        if (serviceProcess is null)
        {
            throw new InvalidOperationException(
                $"Failed to start the SPACE GASS API service from {ServiceExePath}.");
        }

        // == Step 3 — Wait =========================================
        await WaitForServiceReadyAsync(client, TimeSpan.FromSeconds(30));
        Console.WriteLine("Service is ready.");
    }

    // == Do work against the live service ==========================
    var info = await client.Service.Info.GetAsync();
    Console.WriteLine();
    Console.WriteLine($"Connected to SPACE GASS {info?.SpaceGassVersion}");
    Console.WriteLine($"  API path: {info?.ApiPath}");
    Console.WriteLine();
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
    // == Step 4 — Stop (only if we started it) =====================
    if (serviceProcess is not null && !serviceProcess.HasExited)
    {
        Console.WriteLine("Stopping the service...");
        serviceProcess.Kill(entireProcessTree: true);
        serviceProcess.WaitForExit();
        Console.WriteLine("Service stopped.");
    }
}

return 0;


// -- Helpers ------------------------------------------------------

static async Task<bool> IsServiceReadyAsync(SpaceGassApiClient c)
{
    try
    {
        await c.Service.Info.GetAsync();
        return true;
    }
    catch
    {
        return false;
    }
}

static async Task WaitForServiceReadyAsync(SpaceGassApiClient c, TimeSpan timeout)
{
    var deadline = DateTime.UtcNow + timeout;
    while (DateTime.UtcNow < deadline)
    {
        if (await IsServiceReadyAsync(c)) return;
        await Task.Delay(500);
    }
    throw new TimeoutException("SPACE GASS API service did not become ready in time.");
}
