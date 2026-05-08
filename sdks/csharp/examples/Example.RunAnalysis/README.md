# Example.RunAnalysis

Opens an existing `.sg` project, runs a linear static analysis, polls for completion, then prints a summary of the results plus the first few node reactions.

Demonstrates the end-to-end async-job pattern: `POST /run-linear` returns a run handle, `GET /runs/{runId}` polls the status, terminal states are `Completed`, `Failed`, or `Cancelled`.

## Run it

1. Edit `Program.cs` and set `project_file_path` to point at a `.sg` file with structure and loads defined.
2. Start the SPACE GASS API service.
3. From this folder:
   ```
   dotnet run
   ```

See also: [Running Analysis guide](https://spacegass.github.io/space-gass-api/guides/running-analysis).
