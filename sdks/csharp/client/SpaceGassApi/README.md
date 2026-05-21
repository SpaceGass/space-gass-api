# SpaceGassApi

Official .NET SDK for the SPACE GASS structural analysis API.

## Quick Start

```csharp
using SpaceGassApi;
using SpaceGassApi.Models;

var client = SpaceGassApiClient.CreateClient();

// Create a new project
await client.Job.New.PostAsync(new NewPostRequestBody());

// Add a node
var node = await client.Job.Structure.Nodes.PostAsync(
    new NodeCreate { X = 0, Y = 0, Z = 0 });

// Close the project
await client.Job.Close.PostAsync();
```

## Documentation

- [Getting Started](https://api.spacegass.com/docs/)
- [API Reference](https://api.spacegass.com/docs/api)
- [Examples](https://github.com/Spacegass/space-gass-api/tree/main/sdks/csharp/examples)
