# DroneGuard — Judge Walkthrough

**Challenge:** HTCJ × PROOF Aviation Futures Challenge  
**Live demo:** https://u19725505-star.github.io/DroneGuard/  
**Repository:** https://github.com/u19725505-star/DroneGuard  
**Stage:** Interactive prototype / demo-ready interface; not pilot-ready.

## 90-second project explanation

DroneGuard is a JARVIS-inspired mission console concept for drone operations. It brings mission overview, telemetry-style signals, illustrative anomaly scenarios, evidence review, and a 3D browser scene into one interface. The goal is to explore how an operator might move from observing a mission event to inspecting context and documenting the next validation step.

The current hosted version uses synthetic/demo data. It is not connected to a real aircraft, live MAVLink, a validated computer-vision model, or a completed PX4/Gazebo flight. The prototype demonstrates an interface and workflow—not operational flight capability.

## Live walkthrough (about 3–4 minutes)

1. **Mission Map — establish context.** Point out the mission overview and event timeline. Explain that displayed mission events are illustrative.
2. **Telemetry Lab — inspect signals.** Show the telemetry-style panels and explain that values are demo data, not live sensor readings.
3. **Anomaly Intelligence — examine a scenario.** Open the synthetic anomaly view. Describe how an operator could inspect a flagged event, then clearly state that no trained or validated detector is being claimed.
4. **Evidence & Response — connect finding to follow-up.** Show the simulated evidence and response workflow. Emphasize that this is a prototype workflow, not an approved operational procedure.
5. **3D Mission Simulator — demonstrate interaction.** Use the available start/pause/reset and fault-demo controls. Explain that this is an illustrative browser scene, not a PX4 flight recording.
6. **Close with the boundary and next milestone.** No vehicle commands are sent. The next proof milestone is a reproducible PX4 SITL + Gazebo run, captured with software versions, launch steps, visible aircraft motion, and separately identified telemetry.

## How DroneGuard maps to the judging rubric

| Criterion | What this prototype can show honestly | Evidence still needed |
|---|---|---|
| Problem Relevance — 20% | A coherent mission-monitoring and anomaly-review use case for drone/UAS operations | Interviews or feedback from drone operators / inspection teams |
| Innovation + Differentiation — 15% | A unified, cinematic multi-view workflow linking mission context, simulated alerts, and evidence review | Comparative evaluation against existing ground-control and inspection workflows |
| Technical Execution — 20% | Hosted static web app, navigation across five views, interactive UI controls, Three.js visualization, Pages deployment | Automated interaction checks, accessibility review, robust error handling, live-data integration only if safely implemented |
| PROOF / Demonstration — 20% | Reviewers can interact with the live browser prototype and inspect its synthetic scenarios | Recorded demo video; reproducible PX4/Gazebo evidence before claiming simulator integration |
| Pilot Readiness + Feasibility — 15% | A bounded, simulation-first concept with a read-only development path documented in the repo | Controlled SITL validation, alert validation, privacy/security review, aviation expert review, operational requirements |
| Impact + Commercial Potential — 10% | Potential relevance to drone operators, infrastructure inspection teams, and mission supervisors | User discovery, quantified value hypothesis, pilot partner, cost and deployment model |

## Evidence and claim boundaries

**Implemented in the current demo**
- Browser-based multi-view dashboard.
- Mission, telemetry-style, anomaly, evidence, and 3D scenario views.
- Interactive illustrative scenario controls.
- GitHub Pages publication.

**Not established by the current demo**
- Live flight or live telemetry.
- PX4/Gazebo integration running end-to-end.
- A trained computer-vision or anomaly-detection model.
- Detection accuracy, false-alarm rate, or validated safety benefit.
- Aviation certification or operational approval.
- A completed real-world pilot.

Please do not describe synthetic labels, generated alerts, or animated scene behavior as real sensor detections or actual flight evidence.

## Suggested demo recording

If recording a walkthrough, capture the actual browser at the live URL and narrate the steps above. Keep the synthetic/demo label visible. Do not add stock footage or dashboard animation in a way that could be mistaken for a real PX4/Gazebo flight. If a simulator recording is later added, identify the simulator version, world, route, recording method, and what was actually connected.

## Next validation milestone

1. Reproduce the official PX4 SITL + Gazebo baseline in a supported environment.
2. Record versions, commands, environment details, and any setup errors.
3. Validate the custom world separately and show that it loads.
4. Capture the simulated aircraft visibly moving.
5. If telemetry is collected, label its source and keep it distinct from browser demo values.
6. If anomaly detection is added, document dataset provenance, labels, evaluation split, metrics, false positives, false negatives, and limitations.
7. Seek feedback from drone operators and aviation/safety experts before any pilot proposal.

## Reviewer links

- [Open live dashboard](https://u19725505-star.github.io/DroneGuard/)
- [Browse repository](https://github.com/u19725505-star/DroneGuard)
- [PX4 Linux development environment](https://docs.px4.io/main/en/dev_setup/dev_env_linux_ubuntu.html)
- [PX4 Gazebo simulation](https://docs.px4.io/main/en/sim_gazebo_gz/)
- [HTCJ × PROOF Aviation Futures Challenge](https://htcj-aviation-futures.devpost.com/)

**Bottom line:** DroneGuard is a demonstrable interface prototype with a clearly defined path to technical validation. It should be judged as that—not as a completed autonomous drone system.
