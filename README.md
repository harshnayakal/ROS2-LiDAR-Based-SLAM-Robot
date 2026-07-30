# 🤖 ROS2 LiDAR-Based SLAM Robot

A ROS2-based autonomous mobile robot that performs Simultaneous Localization and Mapping (SLAM) using LiDAR. The project uses TurtleBot3, Gazebo, SLAM Toolbox, RViz2, and Nav2 to create maps, localize the robot, and navigate autonomously in a simulated environment.

> **Project Developers**
>
> - Harshvardhan Nayakal
> - Sakshi Patil

---

# 📖 Project Overview

This project demonstrates how a mobile robot can build a map of an unknown environment using LiDAR and later use the saved map for localization and autonomous navigation.

The robot is simulated in Gazebo and visualized in RViz2 using the ROS2 Humble framework.

---

# 🎯 Objectives

- Create a ROS2 SLAM workspace
- Simulate TurtleBot3 in Gazebo
- Build a map using LiDAR
- Save the generated map
- Localize the robot using AMCL
- Navigate autonomously using Nav2
- Understand ROS2 topics, nodes, TF, and navigation

---

# 🚀 Features

- ROS2 Humble based project
- TurtleBot3 mobile robot simulation
- LiDAR-based environment mapping
- SLAM Toolbox integration
- Map saving and loading
- AMCL localization
- Autonomous navigation using Nav2
- RViz2 visualization
- Gazebo simulation

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| ROS2 Humble | Robot middleware |
| Python | ROS2 development |
| TurtleBot3 | Mobile robot |
| Gazebo | Robot simulation |
| RViz2 | Visualization |
| SLAM Toolbox | Mapping |
| Nav2 | Autonomous navigation |
| AMCL | Localization |
| LiDAR | Environment sensing |
| TF2 | Coordinate transformations |

---

# 🏗 System Architecture

```text
                ROS2 Humble
                     │
                     ▼
              TurtleBot3 Robot
                     │
              LiDAR Sensor
                     │
                     ▼
              SLAM Toolbox
                     │
              Occupancy Grid Map
                     │
          Save Map (.pgm/.yaml)
                     │
                     ▼
               Map Server
                     │
                     ▼
                  AMCL
                     │
                     ▼
                  Nav2
                     │
          Global & Local Planner
                     │
                     ▼
             Autonomous Navigation
```

---

# 🔄 Project Workflow

```text
Launch Gazebo
      │
      ▼
Launch SLAM Toolbox
      │
      ▼
Open RViz2
      │
      ▼
Drive Robot
      │
      ▼
Generate Map
      │
      ▼
Save Map
      │
      ▼
Launch Navigation2
      │
      ▼
Set Initial Pose
      │
      ▼
Send Goal
      │
      ▼
Robot Navigates Autonomously
```

---

# 📂 Project Structure

```text
ROS2-LiDAR-Based-SLAM-Robot/

├── lidar_slam_ws/
│
├── src/
│
├── maps/
│   ├── my_slam_map.pgm
│   └── my_slam_map.yaml
│
├── screenshots/
│
├── README.md
└── LICENSE
```

---

# 💻 Requirements

- Ubuntu 22.04
- ROS2 Humble
- TurtleBot3 Packages
- Gazebo
- RViz2
- Navigation2
- SLAM Toolbox
- Python 3

---

# 🚀 Running the Project

## Terminal 1

```bash
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

---

## Terminal 2

```bash
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger

ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True
```

---

## Terminal 3

```bash
source /opt/ros/humble/setup.bash

rviz2
```

Set the Fixed Frame to:

```text
map
```

---

## Terminal 4

```bash
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger

ros2 run turtlebot3_teleop teleop_keyboard
```

Drive the robot to build the map.

---

# Save the Map

```bash
mkdir -p ~/lidar_slam_ws/maps

ros2 run nav2_map_server map_saver_cli -f ~/lidar_slam_ws/maps/my_slam_map
```

---

# Autonomous Navigation

Launch Gazebo:

```bash
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Launch Navigation2:

```bash
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_navigation2 navigation2.launch.py \
map:=/home/vboxuser/lidar_slam_ws/maps/my_slam_map.yaml \
use_sim_time:=True
```

Open RViz2:

```bash
source /opt/ros/humble/setup.bash

rviz2
```

Set:

- Fixed Frame = map
- 2D Pose Estimate
- Nav2 Goal

The robot will localize itself and navigate autonomously to the selected destination.

---

# Verification Commands

Check nodes:

```bash
ros2 node list
```

Check topics:

```bash
ros2 topic list
```

Check navigation actions:

```bash
ros2 action list
```

Check localization:

```bash
ros2 topic echo /amcl_pose --once
```

Check TF:

```bash
ros2 run tf2_ros tf2_echo map base_link
```

---

# Learning Outcomes

Through this project we learned:

- ROS2 workspace creation
- ROS2 package management
- TurtleBot3 simulation
- LiDAR data processing
- SLAM Toolbox
- Occupancy grid mapping
- Map saving
- AMCL localization
- Navigation2
- RViz2 visualization
- TF2 transformations
- Autonomous mobile robot navigation

---

# Future Improvements

- Dynamic obstacle avoidance
- Multi-floor mapping
- 3D LiDAR support
- Multi-robot SLAM
- Autonomous exploration
- Real robot deployment
- Cloud map storage
- Web monitoring dashboard
- AI-assisted path planning

---

# Project Status

- ✅ ROS2 Workspace
- ✅ TurtleBot3 Simulation
- ✅ LiDAR Integration
- ✅ SLAM Toolbox
- ✅ Map Generation
- ✅ Map Saving
- ✅ AMCL Localization
- ✅ Nav2 Integration
- ✅ Autonomous Navigation
- 🔄 Additional feature enhancements in progress

---

# Authors

### Harshvardhan Nayakal

- ROS2 Development
- SLAM Integration
- Navigation2
- Autonomous Navigation
- Python Programming

### Sakshi Patil

- ROS2 Development
- Gazebo Simulation
- RViz2 Visualization
- Testing
- Project Documentation

---

# License

This project is released under the MIT License.

---

# Acknowledgements

This project was developed for learning and demonstrating autonomous mobile robotics using ROS2. It leverages the open-source ROS2 ecosystem, including TurtleBot3, SLAM Toolbox, Nav2, Gazebo, and RViz2. :contentReference[oaicite:0]{index=0}
