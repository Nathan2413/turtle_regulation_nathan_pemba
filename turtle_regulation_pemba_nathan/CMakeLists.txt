cmake_minimum_required(VERSION 2.8.3)
project(turtle_regulation_pemba_nathan1)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  turtlesim
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS rospy std_msgs geometry_msgs turtlesim
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS src/set_way_point.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY srv
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

