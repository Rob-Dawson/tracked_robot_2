Cloned from tracked_robot repo with significant changed. Easier to setup another repo.

**Included:**

World files empty and containing objects

URDF and XACRO of Current Robot 

Meshes

**Plugins including:**
SimpleTrackedController

GazeboROS2TrackedInterface (Source code seperate see gazebo_ros2_tracked_vehicle_interface)
This is needed to provide an interface between gazebo and ROS2 allowing the robot to be controlled from a ROS2 publisher and subscriber. 

Keyboard (For testing)

Joint controller

TODO:

Joint Controller:

This needs implementing properly with PID controller to stop erratic behaviour

GazeboROS2TrackedInterface:

   Implement Odometry
