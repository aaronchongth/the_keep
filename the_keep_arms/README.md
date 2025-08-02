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

Test teleoperation with API.

```bash

```

