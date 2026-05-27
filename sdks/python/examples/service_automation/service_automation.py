"""
Example: Service Automation

Mirrors the Service Automation guide in the Zudoku docs site.
Demonstrates the four-step service lifecycle:

  1. Probe  — try Service.Status to see if the service is already running
  2. Start  — if not, launch SpaceGassApi.exe as a child process
  3. Wait   — poll Service.Status until it responds (or fail with a timeout)
  4. Stop   — terminate the child process when done, but only if we
              started it ourselves

Update SERVICE_EXE below to match your SPACE GASS installation.

Prerequisites:
  - SPACE GASS installed locally
  - SPACE GASS has been opened at least once to initialise data files
"""

import asyncio
import signal
import subprocess
import sys
import time

from space_gass_api import SpaceGassApiClient

SERVICE_EXE = r"C:\Program Files\SPACE GASS 14.5\SpaceGassApi.exe"


async def is_service_ready(client) -> bool:
    try:
        await client.service.status.get()
        return True
    except Exception:
        return False


async def wait_for_service_ready(client, timeout: float = 30.0) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if await is_service_ready(client):
            return
        await asyncio.sleep(0.5)
    raise TimeoutError("SPACE GASS API service did not become ready in time.")


async def main() -> int:
    client = SpaceGassApiClient.create_client("http://localhost:34560")
    process: subprocess.Popen | None = None

    # Hook Ctrl+C so the service still shuts down on a hard interrupt
    def _shutdown(*_):
        if process is not None and process.poll() is None:
            print("\nCtrl+C received — stopping the service...")
            process.terminate()

    signal.signal(signal.SIGINT, _shutdown)
    signal.signal(signal.SIGTERM, _shutdown)

    try:
        # == Step 1 — Probe ============================================
        if await is_service_ready(client):
            print("Service was already running — reusing it.")
        else:
            # == Step 2 — Start ========================================
            print(f"Starting the SPACE GASS API service: {SERVICE_EXE}")
            process = subprocess.Popen(
                [SERVICE_EXE],
                creationflags=subprocess.CREATE_NO_WINDOW,
            )

            # == Step 3 — Wait =========================================
            await wait_for_service_ready(client)
            print("Service is ready.")

        # == Do work against the live service ==========================
        info = await client.service.status.get()
        print()
        print(f"Connected to SPACE GASS {info.space_gass_version}")
        print(f"  API path: {info.api_path}")
        print()

    except Exception as ex:
        print(f"Error: {ex}", file=sys.stderr)
        return 1

    finally:
        # == Step 4 — Stop (only if we started it) =====================
        if process is not None and process.poll() is None:
            print("Stopping the service...")
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
            print("Service stopped.")

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
