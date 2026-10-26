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

This repository currently contains the robot's ROS 2 description package, `cmake_package`. It provides:

- A modular URDF/xacro model of the robot
- STL meshes for the chassis, wheels, castors, lidar, and solar panel
- An RViz configuration and launch file for visualising the model

Autonomy, battery management, and the Raspberry Pi/microcontroller integration are planned but not yet implemented. The current model is two driven wheels plus two castors; the pitch describes the target design as a four-wheel autonomous ground vehicle.

## Repository layout

```text
.
├── cmake_package/
│   ├── CMakeLists.txt
│   ├── package.xml
│   └── src/
│       ├── launch/            # display.launch.py
│       ├── meshes/            # STL meshes
│       ├── rviz/              # RViz configuration
│       └── urdf/              # Modular xacro files
└── pitchdeck/
    └── MoSH-B Mobile Solar Harnessing Bot.pptx
```

## Quick start

```bash
git clone https://github.com/zane1502/mosh-b-asap-group-2.git
cd mosh-b-asap-group-2
source /opt/ros/$ROS_DISTRO/setup.bash
colcon build --symlink-install
source install/setup.bash
ros2 launch cmake_package display.launch.py
```

## Roadmap

- [x] URDF/xacro robot description
- [x] RViz visualisation with movable joints
- [ ] Raspberry Pi software stack
- [ ] Microcontroller integration for motors and sensors
- [ ] Autonomous navigation and delivery workflow
- [ ] Sun-tracking control using light sensors
- [ ] Battery pack and BESS integration
- [ ] Prototype build and community pilot
