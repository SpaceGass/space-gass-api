# service_automation

Probes for an already-running SPACE GASS API service; if none is found, launches `SpaceGassApi.exe` as a child process, waits for it to become ready, fetches `service.info` to confirm, and shuts the service down on exit (only if this script started it).

The probe + start + wait + stop lifecycle for any script or batch job that wants to manage the service itself rather than relying on the user to start it manually.

## Run it

1. Edit `service_automation.py` and set `SERVICE_EXE` to the SPACE GASS install path on this machine (default `C:\Program Files\SPACE GASS 14.5\SpaceGassApi.exe`).
2. Install dependencies:
   ```
   pip install space-gass-api
   ```
3. From this folder:
   ```
   python service_automation.py
   ```

See also: [Service Automation guide](https://api.spacegass.com/docs/guides/service-automation) for the full pattern including SIGINT handling and custom-port setups.
