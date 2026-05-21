# C# Examples

## In your own project

Install the NuGet package:

```
dotnet add package SpaceGassApi --prerelease
```

Then copy and run any example. Each is a standalone console app.

## From this repo

Examples build against the local SDK source by default:

```
dotnet build SpaceGassApi.Examples.sln
```

This is controlled by [`Directory.Build.props`](Directory.Build.props). To build against the published NuGet package instead:

```
dotnet build -p:UseLocalSdk=false
```
