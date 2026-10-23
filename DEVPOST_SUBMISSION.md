# Devpost Submission Draft — DroneGuard

> Copy the sections below into the HTCJ × PROOF Aviation Futures Challenge submission form. Review every field and add your own demo video or screenshots before submitting.

## Project name

DroneGuard

## Tagline

A JARVIS-inspired mission console for inspecting drone mission context, simulated anomalies, and evidence in one place.

## Problem

Drone operators and infrastructure-inspection teams need a clear way to understand mission status and investigate potential issues. When status, signals, and follow-up evidence are spread across different views, an operator can lose context. A useful mission console should make the event, its context, and the next validation step easy to follow—without implying that an unverified alert is ground truth.

## Solution

DroneGuard is a simulation-first, interactive browser prototype that brings five views into one mission-console experience: Mission Map, Telemetry Lab, Anomaly Intelligence, Evidence & Response, and a 3D Mission Simulator. A reviewer can explore an illustrative mission, inspect synthetic anomaly scenarios, and follow the path from observation to documentation and planned validation.

The design is inspired by cinematic AI copilots, but the project keeps a strict boundary between an interface concept and operational capability. The hosted demo does not control a drone or connect to live telemetry.

## What can be demonstrated today?

- A publicly accessible browser dashboard with five navigable views.
- Interactive controls for the illustrative 3D mission scenario.
- Synthetic/demo anomaly and evidence workflows.
- A published GitHub repository with setup notes, a read-only telemetry-probe scaffold, a future PX4/Gazebo validation path, and a judge walkthrough.

**Important evidence boundary:** The current demo does not establish a completed PX4/Gazebo flight, live MAVLink integration, a trained or validated computer-vision model, anomaly-detection accuracy, or aviation certification. Synthetic values and alerts are clearly presented as demonstration content.

## Live demo

https://u19725505-star.github.io/DroneGuard/

## Source code

https://github.com/u19725505-star/DroneGuard

## Supporting documentation

- Judge walkthrough: https://github.com/u19725505-star/DroneGuard/blob/main/JUDGE_GUIDE.md
- README and technical scope: https://github.com/u19725505-star/DroneGuard/blob/main/README.md

## Technology used

- HTML, CSS, and JavaScript
- Three.js (loaded from a public CDN) for the illustrative 3D scene
- GitHub Pages for static hosting
- GitHub Actions for deployment
- PX4 SITL / Gazebo are documented as a future validation path, not a completed end-to-end integration

## Target users

Potential users include drone mission supervisors, UAS operators, and infrastructure-inspection teams who need to review mission events and organize follow-up evidence. This target-user hypothesis still needs validation through operator interviews and workflow feedback.

## Current project stage

Interactive prototype / demo-ready interface. Not pilot-ready.

## What makes it different?

DroneGuard combines a cinematic multi-view mission console with a visible path from mission context to anomaly inspection and evidence review. Its current differentiator is the integrated demonstration workflow and explicit evidence boundaries, rather than a claim of novel or validated AI performance.

## Deployment and business path

A credible next step is a controlled evaluation with drone operators using recorded or simulated mission data. The team would first validate the dashboard workflow and data provenance, then assess whether a read-only connection to a supported simulator can be added safely. Any future pilot would require technical validation, security/privacy review, aviation expertise, and applicable regulatory review. No customer deployment or paid integration is claimed today.

## Next milestone

Reproduce a supported PX4 SITL + Gazebo baseline, document versions and launch steps, show the simulator world loading and aircraft moving, and keep real simulator telemetry separate from browser demo values. If a detection model is later introduced, report its data sources, evaluation method, false positives, false negatives, and limitations.

## Team

Independent project by **John Constantine**. Add any actual collaborators here if applicable. Do not list people as team members without their agreement.

## Video and screenshots checklist

Before submission:
- [ ] Add a short screen recording of the live dashboard, keeping synthetic/demo labels visible.
- [ ] Include one screenshot showing the multi-view dashboard.
- [ ] Include one screenshot of the 3D Mission Simulator.
- [ ] Include one screenshot of Anomaly Intelligence or Evidence & Response.
- [ ] Verify the live URL from a private/incognito browser session.
- [ ] Confirm the project name, team details, and any required challenge fields.
- [ ] Do not imply the browser simulation is actual flight footage.
