# Example.ServiceAutomation

Probes for an already-running SPACE GASS API service; if none is found, launches `SpaceGassApi.exe` as a child process, waits for it to become ready, fetches `Service.Info` to confirm, and shuts the service down on exit (only if this script started it).

The probe + start + wait + stop lifecycle for any script or batch job that wants to manage the service itself rather than relying on the user to start it manually.

## Run it

1. Edit `Program.cs` and set `ServiceExePath` to the SPACE GASS install path on this machine (default `C:\Program Files\SPACE GASS 14.5\SpaceGassApi.exe`).
2. From this folder:
   ```
   dotnet run
   ```

See also: [Service Automation guide](https://spacegass.github.io/space-gass-api/guides/service-automation) for the full pattern including Ctrl+C handling and custom-port setups.
