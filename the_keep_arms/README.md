## Set up calibration files

Set up devices.

```bash
# leader
sudo chmod 666 /dev/ttyACM0

# follower
sudo chmod 666 /dev/ttyACM1
```

Calibrate or copy over the calibrated values.

```bash
mkdir -p  ~/.cache/huggingface/lerobot/calibration/teleoperators/so101_leader/
cp config/my_awesome_leader_arm.json  ~/.cache/huggingface/lerobot/calibration/teleoperators/so101_leader/my_awesome_leader_arm.json

mkdir -p ~/.cache/huggingface/lerobot/calibration/robots/so101_follower/
cp config/my_awesome_follower_arm.json ~/.cache/huggingface/lerobot/calibration/robots/so101_follower/my_awesome_follower_arm.json
```

Test teleoperation.

```bash
python -m lerobot.teleoperate \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.id=my_awesome_follower_arm \
  --teleop.type=so101_leader \
  --teleop.port=/dev/ttyACM0 \
  --teleop.id=my_awesome_leader_arm
```

Test teleoperation with camera.

```bash
python -m lerobot.teleoperate \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.id=my_awesome_follower_arm \
  --robot.cameras="{ right: {type: intelrealsense, serial_number_or_name: '049122252220', fps: 15, width: 640, height: 480, use_depth: True, rotation: 0, color_mode: rgb } }" \
  --teleop.type=so101_leader \
  --teleop.port=/dev/ttyACM0 \
  --teleop.id=my_awesome_leader_arm \
  --display_data=true
```

Record dataset.

```bash
python -m lerobot.record \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.id=my_awesome_follower_arm \
  --robot.cameras="{ right: {type: intelrealsense, serial_number_or_name: '049122252220', fps: 15, width: 640, height: 480, use_depth: True, rotation: 0, color_mode: rgb } }" \
  --teleop.type=so101_leader \
  --teleop.port=/dev/ttyACM0 \
  --teleop.id=my_awesome_leader_arm \
  --display_data=true \
  --dataset.repo_id=${HF_USER}/record-test \
  --dataset.num_episodes=2 \
  --dataset.single_task="Grab the 2x2 cube"
```

Run inference.

```bash
python -m lerobot.record \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.id=my_awesome_follower_arm \
  --robot.cameras="{ right: {type: intelrealsense, serial_number_or_name: '049122252220', fps: 15, width: 640, height: 480, use_depth: True, rotation: 0, color_mode: rgb } }" \
  --display_data=true \
  --dataset.repo_id=${HF_USER}/eval_record-test \
  --dataset.episode_time_s=50 \
  --dataset.num_episodes=10 \
  --dataset.single_task="Eval grab the 2x2 cube" \
  --policy.path=${HF_USER}/my_smolvla \
  --policy.device=cuda
```
