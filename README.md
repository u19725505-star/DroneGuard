# DroneGuard

**A JARVIS-inspired, simulation-first mission console for drone operations.**

[**Open the live dashboard**](https://u19725505-star.github.io/DroneGuard/) · [Judge walkthrough](JUDGE_GUIDE.md) · [Source code](https://github.com/u19725505-star/DroneGuard)

DroneGuard explores how a mission operator could review a drone mission, inspect telemetry-style signals, understand simulated anomalies, and follow an evidence-oriented response workflow through one browser interface. It is a prototype for **AI + Flight Intelligence** and **Autonomy + Advanced Air Mobility** workflows in the HTCJ × PROOF Aviation Futures Challenge.

> **Truth-in-demo notice:** The hosted dashboard is a browser-based prototype using illustrative/synthetic mission data. It is not connected to a live aircraft, live MAVLink telemetry, a deployed computer-vision model, or a validated PX4/Gazebo flight. A cinematic visualization is not evidence of a real flight. No vehicle commands are sent.

## The problem

Drone operators and inspection teams need to make sense of mission status, potential anomalies, and follow-up evidence without losing context across separate tools. A polished interface alone does not solve that operational problem; the information must be understandable, traceable, and validated against real systems before it can support flight decisions.

## The proposed solution

DroneGuard brings a mission-console concept into one interactive browser experience:

- **Mission Map** — a mission overview and event timeline.
- **Telemetry Lab** — inspect illustrative flight-state signals and scenario behavior.
- **Anomaly Intelligence** — explore synthetic alerts and their context.
- **Evidence & Response** — organize the simulated finding and a follow-up response workflow.
- **3D Mission Simulator** — interact with a visual mission scenario, including start, pause, reset, and fault-demo controls.

The interface is designed to help a reviewer follow a clear loop: **observe → inspect → interpret → document → plan validation**. Current anomaly labels and metrics are demonstrative, not validated detection results.

## Live demo

**Dashboard:** https://u19725505-star.github.io/DroneGuard/

1. Open the dashboard and keep the DEMO / synthetic-data status in view.
2. Visit each of the five views using the navigation tabs.
3. In the 3D Mission Simulator, use the scenario controls to inspect the illustrative sequence. Use the fault control to demonstrate the UI's anomaly-response presentation.
4. Visit Anomaly Intelligence and Evidence & Response to see how a synthetic alert can be inspected and carried into a follow-up workflow.
5. Finish with the safety boundary: the current site does not arm, steer, or command an aircraft.

A step-by-step presenter script and the evidence boundaries are documented in [JUDGE_GUIDE.md](JUDGE_GUIDE.md).

## Current implementation and limits

| Capability | Current status |
|---|---|
| Hosted interactive dashboard | Published through GitHub Pages |
| Multi-view mission console | Implemented in the browser UI |
| 3D scenario and UI controls | Illustrative browser simulation |
| Anomaly and evidence workflow | Synthetic/demo scenarios |
| Live PX4 or Gazebo integration | **Not demonstrated / not claimed** |
| Live MAVLink data in the hosted page | **Not connected** |
| Trained or validated computer-vision model | **Not included / not claimed** |
| Flight-safety or airworthiness certification | **Not certified** |
| Real-world pilot | **Not completed** |

The repository also contains an early PX4/Gazebo scene-validation scaffold and a read-only telemetry probe. These are development starting points, not proof that a custom urban world has been launched successfully or that live telemetry has been integrated into the hosted dashboard.

## Technology

- HTML, CSS, and JavaScript for the browser interface.
- Three.js loaded from a public CDN for the illustrative 3D scene.
- GitHub Pages for static hosting.
- GitHub Actions for publishing the dashboard.
- PX4 SITL / Gazebo integration is a planned validation path; it should not be described as a completed integration until it has been run and documented.

The dashboard requires an internet connection to load the Three.js module from the CDN. No paid API is required by the hosted demo. GitHub Actions usage is subject to the account's current included minutes and storage limits.

## Repository map

- index.html — root entry point, synchronized with the deployed dashboard.
- web/index.html — dashboard source used by the Pages workflow.
- worlds/urbanscape.sdf — procedural city-block world for future scene validation.
- scripts/telemetry_probe.py — read-only local MAVLink telemetry probe.
- .github/workflows/pages.yml — publishes web/index.html to GitHub Pages.
- JUDGE_GUIDE.md — reviewer walkthrough, rubric mapping, and evidence boundaries.

## Local PX4/Gazebo validation path

This is a future validation path, not a claim of completed integration.

Official references:
- [PX4 Linux development environment](https://docs.px4.io/main/en/dev_setup/dev_env_linux_ubuntu.html)
- [PX4 Gazebo simulation](https://docs.px4.io/main/en/sim_gazebo_gz/)

On a supported Ubuntu environment with PX4 dependencies installed, first validate the official baseline:

```bash
cd PX4-Autopilot
make px4_sitl gz_x500
```

Only after the baseline works should the custom world be tested separately with the Gazebo version supported by the installed PX4 release. SDF files, model names, and launch mechanisms can vary between versions; do not assume the included world is already wired into a successful PX4 flight.

### Read-only telemetry probe

Install pymavlink in the intended Python environment, then use the endpoint configured by your local SITL setup:

```bash
python -m pip install pymavlink
python scripts/telemetry_probe.py --endpoint udp:127.0.0.1:14540 --seconds 8
```

The probe is intended to print received telemetry only. It does not send arm, takeoff, mission, or movement commands. Confirm the correct local endpoint for your setup; ports vary.

## Safety and responsible use

- Simulation/demo only; do not use this prototype to make live flight decisions.
- Do not expose MAVLink endpoints to the public internet.
- Do not enter private operational information into a public demo.
- No real person, thermal detection, or operational emergency is asserted by the synthetic scenarios.
- Any future real-world test would require controlled simulation or test conditions, validated data and alerts, appropriate aviation expertise, privacy/security review, and applicable regulatory review.

## Project stage and next proof milestone

**Stage: interactive prototype / demo-ready interface. Not pilot-ready.**

The most valuable next proof is a reproducible, recorded test in a supported PX4 SITL + Gazebo environment: document the software versions and launch commands, show the world loading and simulated aircraft moving, capture real telemetry separately from demo values, and record the source and validation method for any anomaly detector. Do not present dashboard animation or synthetic alerts as evidence of those milestones.

## Challenge alignment

DroneGuard maps most directly to the challenge's **AI + Flight Intelligence** and **Autonomy + Advanced Air Mobility** areas. Its present contribution is an interactive mission-monitoring concept and a transparent demonstration workflow—not a claim of a novel, validated AI model or operational drone-control system.

## License

MIT. See [LICENSE](LICENSE).
