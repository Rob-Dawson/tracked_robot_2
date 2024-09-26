cmake_minimum_required(VERSION 3.8)
project(tracked_robot_2)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rclcpp REQUIRED)
find_package(ignition-math6 REQUIRED)
find_package(gazebo REQUIRED)
find_package(Boost REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
#Custom package for using ROS2 with tracked robots
# find_package(gazebo_ros2_tracked_vehicle_interface)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)

  set(ament_cmake_copyright_FOUND TRUE)

  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_python_install_package(${PROJECT_NAME})


# add_library(gazebo_track_interface SHARED src/gazebo_ros_tracked_vehicle_interface.cpp)

# include_directories()

# target_include_directories(gazebo_track_interface PUBLIC
#   $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
#   $<INSTALL_INTERFACE:include>)

# ament_target_dependencies(gazebo_track_interface
# "rclcpp"
# "gazebo_ros"
# "nav_msgs"
# "tf2_ros"
# )

# install(TARGETS gazebo_track_interface
#   DESTINATION share/${PROJECT_NAME})

  # Install header files
install(DIRECTORY include/
  DESTINATION include/${PROJECT_NAME})

#Install All other files  
install(DIRECTORY scripts config worlds description description/meshes launch
  DESTINATION share/${PROJECT_NAME})

# Ament package exports
ament_export_include_directories(include)
ament_export_libraries(robot_controller)
ament_export_dependencies(rclcpp gazebo_dev)

ament_package()


