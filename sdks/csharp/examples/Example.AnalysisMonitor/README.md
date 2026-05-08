# Example.AnalysisMonitor

A more complete sample app — not a tutorial — that runs an analysis on an existing project and renders real-time progress (current step, iteration percentage, load-case status) to a console UI. Demonstrates a richer monitoring loop than `Example.RunAnalysis`.

`net8.0-windows` target — uses Windows-specific console handling for the live progress display.

## Run it

1. Edit `Program.cs` to point at an existing `.sg` project file.
2. Start the SPACE GASS API service.
3. From this folder:
   ```
   dotnet run
   ```

If you just want the basic run + poll pattern without the UI, use [Example.RunAnalysis](../Example.RunAnalysis) instead.
