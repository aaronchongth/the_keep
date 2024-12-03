# The Keep

## Running Open-RMF for tb4

### Start zenoh router on host

```bash
zenohd --rest-http-port 8001
```

### SSH into the tb4

Make sure to get the Create3 to
* use `rmw_cyclonedds_cpp`
* `ROS_DOMAIN_ID` to be 0
* no DDS config file

Final tb4 setup,

```bash
export CYCLONEDDS_URI=""
export FASTRTPS_DEFAULT_PROFILES_FILE="/etc/turtlebot4/fastdds_rpi.xml"
export ROBOT_NAMESPACE=""
export ROS_DOMAIN_ID="0"
export ROS_DISCOVERY_SERVER=""
export RMW_IMPLEMENTATION="rmw_cyclonedds_cpp"
export TURTLEBOT4_DIAGNOSTICS="1"
export WORKSPACE_SETUP="/opt/ros/humble/setup.bash"
export ROS_SUPER_CLIENT="False"
```

This way the Create3 and Turtlebot4 Raspberry pi will have the same local setup,

```bash
git clone https://github.com/aaronchongth/the_keep
git clone https://github.com/open-rmf/free_fleet
```

Run localization with map,

```bash
ros2 launch turtlebot4_navigation localization.launch.py \
  map:=the_keep/the_keep_maps/maps/the_keep/the_keep.yaml \
  params:=the_keep/the_keep/params/localization.yaml
```

Run navigation,

```bash
ros2 launch turtlebot4_navigation nav2.launch.py
```

Run zenoh bridge,

```bash
./zenoh-bridge-ros2dds -c the_keep/the_keep/zenoh_configs/tb4_client_zenoh_config.json5
```

Other useful commands,

```bash
# Dock
ros2 action send_goal /dock irobot_create_msgs/action/Dock '{}'

# Undock
ros2 action send_goal /undock irobot_create_msgs/action/Undock '{}'
```


### Start Open-RMF on host

Start dashboard,

```bash
docker run \
  --network host -it --rm \
  -e RMF_SERVER_URL=http://localhost:8000 \
  -e TRAJECTORY_SERVER_URL=ws://localhost:8006 \
  ghcr.io/open-rmf/rmf-web/demo-dashboard:latest
```

Start API server,

```bash
docker run \
  --network host -it --rm \
  -e ROS_DOMAIN_ID=55 \
  -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
  ghcr.io/open-rmf/rmf-web/api-server:jazzy
```

Start Open-RMF common,

```bash
# use jazzy, cyclone, domain 55
ros2 launch the_keep tb4_the_keep_rmf_common.launch.xml
```

Start fleet adapter,

```bash
# use jazzy, cyclone, domain 55
ros2 launch the_keep tb4_the_keep_fleet_adapter.launch.xml server_uri:="ws://localhost:8000/_internal"
```
