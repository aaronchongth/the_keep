from lerobot.cameras.configs import ColorMode, Cv2Rotation
from lerobot.cameras.realsense.configuration_realsense import RealSenseCameraConfig
from lerobot.cameras.realsense.camera_realsense import RealSenseCamera
from lerobot.teleoperators.so101_leader import SO101LeaderConfig, SO101Leader
from lerobot.robots.so101_follower import SO101FollowerConfig, SO101Follower

camera_config = {
    "right": RealSenseCameraConfig(
        serial_number_or_name="049122252220",
        fps=15,
        width=640,
        height=480,
        color_mode=ColorMode.RGB,
        use_depth=True,
        rotation=Cv2Rotation.NO_ROTATION
    )
}

robot_config = SO101FollowerConfig(
    port="/dev/ttyACM1",
    id="my_awesome_follower_arm",
    cameras=camera_config
)

teleop_config = SO101LeaderConfig(
    port="/dev/ttyACM0",
    id="my_awesome_leader_arm",
)

robot = SO101Follower(robot_config)
teleop_device = SO101Leader(teleop_config)
robot.connect()
teleop_device.connect()

while True:
    observation = robot.get_observation()
    action = teleop_device.get_action()
    robot.send_action(action)
