cmake_minimum_required(VERSION 3.5)

project(the_keep)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  launch/
  DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY
  fleet_configs/
  DESTINATION share/${PROJECT_NAME}/fleet_configs
)

install(DIRECTORY
  params/
  DESTINATION share/${PROJECT_NAME}/params
)

ament_package()
