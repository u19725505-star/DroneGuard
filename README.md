# DroneGuard

**A PX4 SITL urban-flight lab with a JARVIS-inspired telemetry console.**

DroneGuard is a simulation-only project. It is designed to build a repeatable path from PX4 Software-in-the-Loop (SITL), through a custom Gazebo scene, to an inspectable browser dashboard and recorded flight footage.

> **Safety boundary:** PX4 SITL only. No real aircraft, no physical actuator interfaces, no live vehicle connection. The included browser dashboard is a UI; it does not arm or control a vehicle. Never expose a MAVLink endpoint to the public internet.

## Project goals

1. Establish a reproducible PX4 + Gazebo SITL environment.
2. Add an urban-style Gazebo world and verify that it loads before attempting any flight.
3. Capture actual simulator footage (not a CSS animation presented as simulator output).
4. Show telemetry in a cinematic browser HUD, clearly distinguishing demo values from live simulator values.
5. Keep the workflow free of paid APIs and paid infrastructure. GitHub Actions usage is subject to the account's current included minutes and storage limits; check billing settings before enabling heavy jobs.

## Repository map

- `worlds/urbanscape.sdf` — simple procedural city-block world for scene validation.
- `web/index.html` — static JARVIS-style HUD preview; can be published with GitHub Pages.
- `scripts/telemetry_probe.py` — read-only local MAVLink telemetry probe.
- `.github/workflows/pages.yml` — publishes the static dashboard to GitHub Pages.

## Start here

### 1. Open the dashboard

Open `web/index.html` locally, or enable GitHub Pages with **Settings → Pages → GitHub Actions**. The hosted version runs in **DEMO MODE** by default. A static GitHub Pages site cannot access a process running inside your Kaggle notebook or on your device; live telemetry requires a local bridge and an explicitly configured browser-accessible endpoint.

### 2. Validate PX4 and Gazebo locally

Follow the official PX4 Linux setup and Gazebo simulation guide:
- https://docs.px4.io/main/en/dev_setup/dev_env_linux_ubuntu.html
- https://docs.px4.io/main/en/sim_gazebo_gz/

On a supported Ubuntu environment with PX4 dependencies installed, the official X500 baseline is:

```bash
cd PX4-Autopilot
make px4_sitl gz_x500
```

First verify the baseline simulator and vehicle start successfully. Then validate the custom world separately with the Gazebo version supported by your PX4 setup. World files and model names can vary between Gazebo releases; do not assume the included SDF is automatically wired into PX4's vehicle spawn command.

### 3. Probe local telemetry (read-only)

Install pymavlink in your active Python environment, then run:

```bash
python -m pip install pymavlink
python scripts/telemetry_probe.py --endpoint udp:127.0.0.1:14540 --seconds 8
```

This prints received MAVLink state only. It sends no arm, takeoff, mission, or movement commands. Use the endpoint actually configured by your SITL launch; ports differ by setup.

## Flight-video milestone

Record video only after the city world is visibly loaded and the simulated aircraft is visibly moving in the simulator. A desktop screen recording of a terminal, a static scene, or the dashboard's illustrative skyline is not proof of a rendered flight. Save the original capture and include the simulator version, world, route, and recording method in the video description.

## Current status

This repository provides the first project scaffold, static dashboard, telemetry probe, and a scene-validation world. It does **not** claim a completed urban flight, a validated PX4 custom-world launch, or a finished MP4. Those are milestones to verify in the target environment.

## License

MIT. See `LICENSE`.
