# run_analysis

Opens an existing `.sg` project, runs a linear static analysis, polls for completion, then prints a summary of the results plus the first few node reactions.

Demonstrates the end-to-end async-job pattern: `POST /run-linear` returns a run handle, `GET /runs/{run_id}` polls the status, terminal states are `Completed`, `Failed`, or `Cancelled`.

## Run it

1. Edit `run_analysis.py` and set `project_file_path` to point at a `.sg` file with structure and loads defined.
2. Start the SPACE GASS API service.
3. Install dependencies:
   ```
   pip install space-gass-api
   ```
4. From this folder:
   ```
   python run_analysis.py
   ```

See also: [Running Analysis guide](https://api.spacegass.com/docs/guides/running-analysis).
