# query_restrained_nodes

Opens an existing `.sg` project, filters nodes to only those with restraints (`node_type=Restrained`), then retrieves and prints the reaction results for those nodes — fx, fy, fz, mx, my, mz per (node, case) combination.

Demonstrates SG list-format filtering: nodes are passed as a comma-separated string (`"1,5-10"`) on the query parameter, not an array.

## Run it

1. Edit `query_restrained_nodes.py` and set `PROJECT_FILE_PATH` to point at an analysed `.sg` file.
2. Start the SPACE GASS API service.
3. Install dependencies:
   ```
   pip install space-gass-api
   ```
4. From this folder:
   ```
   python query_restrained_nodes.py
   ```

See also: [Filtering & Querying guide](https://api.spacegass.com/docs/guides/filtering-and-querying).
