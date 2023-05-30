cmake_minimum_required(VERSION 2.8.3)
project(turtle_regulation_pemba_nathan)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
  std_msgs
  geometry_msgs
  turtlesim
)

catkin_package(
  CATKIN_DEPENDS rospy roscpp std_msgs geometry_msgs turtlesim
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(set_way_point src/set_way_point.cpp)
target_link_libraries(set_way_point ${catkin_LIBRARIES})

add_executable(set_way_point_distance src/set_way_point_distance.cpp)
target_link_libraries(set_way_point_distance ${catkin_LIBRARIES})

add_service_files(
  FILES
  waypoint.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_package(
  CATKIN_DEPENDS message_runtime std_msgs
)

add_dependencies(set_way_point turtle_regulation_pemba_nathan_generate_messages_cpp)
add_dependencies(set_way_point_distance turtle_regulation_pemba_nathan1_generate_messages_cpp)
