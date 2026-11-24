# MoSH-B: Mobile Solar Harnessing Bot

MoSH-B is a proof-of-concept mobile robot that delivers stored solar energy to homes with unreliable grid power. It acts as the delivery link in a wider energy system made up of solar panels, a Battery Energy Storage System (BESS), and portable household battery packs.

## The problem

Unstable grid supply leaves residents unable to keep essential devices running. Stored energy may exist at a BESS, but it often does not reach the homes that need it.

## The solution

A self-powered robot that carries charged battery packs from the BESS to residents' homes. While travelling, MoSH-B recharges itself using an onboard sun-tracking solar panel.

## How it works

1. **Store** - Solar panels charge the BESS.
2. **Load** - MoSH-B collects charged battery packs from the BESS.
3. **Deliver** - The robot travels autonomously to residents and hands over the packs.
4. **Power** - Homes run laptops and other essential devices from the packs.

The concept includes a modular cargo rack for 4 to 8 packs, a sun-tracking solar mount, and autonomous operation with little human supervision.

Projected impact from the pitch deck (not yet field-validated):

- About 10 households served per robot per day
- About 4 kWh delivered per trip
- About 10 hours of essential loads per pack

## Current status

All ROS 2 work lives in the `moshb_ws/` colcon workspace. So far it has:

- **`mosh_b_description`**: the robot model exported from SolidWorks. It has two motor-driven wheels, a castor, the drive base, a Raspberry Pi, an L298N motor driver, a buck converter and a lidar. It also includes STL meshes, an RViz view, and Gazebo (Lyrical · Jetty) launch and world files.
- **`mosh_b_bringup`**: empty for now. Top-level launch files and parameters will go here.
- **`mosh_b_control`**: empty for now. Python nodes for motors, sensors and sun tracking will go here.

Autonomy, battery management, and the Raspberry Pi/microcontroller integration are planned but not yet implemented. The solar panel and cargo rack are not in the current model yet. The pitch describes the target design as a four-wheel autonomous ground vehicle.

## Repository layout

```text
.
├── README.md
├── pitchdeck/
│   └── MoSH-B Mobile Solar Harnessing Bot.pptx
└── moshb_ws/                  # ROS 2 workspace
    └── src/
        ├── mosh_b_description/  # URDF, meshes, RViz, Gazebo
        ├── mosh_b_bringup/      # launch + config (empty)
        └── mosh_b_control/      # control nodes (empty)
```

## Quick start

```bash
git clone https://github.com/zane1502/mosh-b-asap-group-2.git MoSH-B
cd MoSH-B/moshb_ws
source /opt/ros/$ROS_DISTRO/setup.bash
rosdep install --from-paths src -y --ignore-src
colcon build --symlink-install
source install/setup.bash
ros2 launch mosh_b_description display.launch.py
```

## Roadmap

- [x] URDF robot description
- [x] RViz visualisation with movable joints
- [ ] Raspberry Pi software stack
- [ ] Microcontroller integration for motors and sensors
- [ ] Autonomous navigation and delivery workflow
- [ ] Sun-tracking control using light sensors
- [ ] Battery pack and BESS integration
- [ ] Prototype build and community pilot
