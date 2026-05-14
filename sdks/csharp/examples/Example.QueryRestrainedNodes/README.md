# Example.QueryRestrainedNodes

Opens an existing `.sg` project, filters nodes to only those with restraints (`NodeType=Restrained`), then retrieves and prints the reaction results for those nodes — Fx, Fy, Fz, Mx, My, Mz per (node, case) combination.

Demonstrates SG list-format filtering: nodes are passed as a comma-separated string (`"1,5-10"`) on the query parameter, not an array.

## Run it

1. Edit `Program.cs` and set `PROJECT_FILE_PATH` to point at an analysed `.sg` file.
2. Start the SPACE GASS API service.
3. From this folder:
   ```
   dotnet run
   ```

See also: [Filtering & Querying guide](https://api.spacegass.com/docs/guides/filtering-and-querying).
