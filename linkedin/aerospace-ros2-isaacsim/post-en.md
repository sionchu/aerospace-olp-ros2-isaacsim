I rebuilt an aerospace drilling OLP workflow with ROS 2 and NVIDIA Isaac Sim.

In aerospace manufacturing, robot programming is not simply about moving from point A to point B.

The real challenge is maintaining a trustworthy geometric chain:

Aircraft datum → fixture/workpiece → robot base → flange → calibrated TCP → hole center and surface normal

Even a highly repeatable robot can miss the CAD target if base registration, joint offsets, TCP calibration, workpiece localization, or frame transformations are incorrect. For drilling, position alone is not enough—the tool also needs to align with the local surface normal.

This is why deterministic offline programming platforms such as DELMIA, and tools such as RoboDK, remain valuable in aerospace manufacturing. They help engineers preserve CAD-to-process traceability, validate reach and collisions, manage coordinate systems, and prepare robot programs without occupying the physical cell.

For this portfolio project, I recreated that rule-based OLP concept using ROS 2 and NVIDIA Isaac Sim.

The digital twin includes:

• An official six-axis UR10e articulation
• A curved aircraft-panel surrogate with 10 DRPE-style drilling locations
• Explicit world, robot-base, TCP, joint, and hole coordinate frames
• Collision-aware task-space motion using cuMotion RMPflow
• A deterministic sequence: Approach → Align → Dock → Clamp → Drill → Verify → Retract
• ROS 2 command, acknowledgement, process-status, J1–J6, and TCP-pose topics
• A trained VLA-lite policy for hole selection within a safety-constrained process
• Repeatable headless tests and a recorded closed-loop trial

In the demonstration, an external ROS 2 terminal publishes RUN_HOLE H01. Isaac Sim accepts the request, executes the complete drilling sequence, and returns live robot and process telemetry through Fast DDS.

My main takeaway is that ROS 2 and Isaac Sim should not be treated as a simple replacement for production OLP.

A stronger architecture combines both approaches:

Deterministic geometry and process rules from OLP, combined with open interfaces, physics-based validation, automated testing, observability, and adaptive robotics capabilities.

This is a simulation prototype, not a production-qualified drilling system. A real deployment would still require physical TCP identification, workpiece localization, robot and cell calibration, force/torque feedback, process qualification, and validation on representative material stacks.

Built and iterated with Codex as a development partner.

Where do you see the right boundary between deterministic OLP and adaptive robotics in aerospace manufacturing?

#AerospaceManufacturing #Robotics #ROS2 #IsaacSim #DigitalTwin #OfflineProgramming
