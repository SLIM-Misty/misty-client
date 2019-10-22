import requests

ip = "10.10.0.7"

""" When moving Misty's arms, it's helpful to understand their orientation.
At 0 degrees, Misty's arms point straight forward along her X axis, parallel to the ground.
At +90 degrees, Misty's arms point straight down towards the ground.
At +/- 180 degrees, Misty's arms would face straight back, pointing toward her backpack; however, Misty's arms are not currently configured to move to this position.
At -90/+270 degrees, Misty's arms would point straight up towards her head, perpendicular to the ground; however, the upward movement of Misty's arm movement is currently limited to -29 degrees.

Parameters
Arm (string) - The arm to move. You must use either left, right, or both.
Position (double) - The new position to move the arm to. Use the Units parameter to determine whether to use position, degrees, or radians. Defaults to degrees.
Velocity (double) - Optional. A value of 0 to 100, specifying the speed with which the arm should move. Defaults to null.
Units (string) - Optional. A string value of degrees, radians, or position that determines which unit to use in moving Misty's arms.
"""

def move_arm(arm, position, velocity=50, units='degrees'):
    parameters = {
        "Arm": arm,
        "Position": position,
        "Velocity": velocity,
        "Units": units
    }
    requests.post("HTTP://" + ip + "/api/arms", json=parameters)

move_arm('left', 29)

def move_arms(left_pos, right_pos, left_vel=50, right_vel=50, units='degrees'):
    parameters = {
        "LeftArmPosition": left_pos,
        "RightArmPosition": right_pos,
        "LeftArmVelocity": left_vel,
        "RightArmVelocity": right_vel,
        "Units": units
    }
    requests.post("HTTP://" + ip + "/api/arms/set", json=parameters)

move_arms(0, -29)


def move_head(pitch, roll, yaw, velocity=50, duration=None, units='degrees'):
    parameters = {
        "Pitch": pitch,
        "Roll": roll,
        "Yaw": yaw,
        "Velocity": velocity,
        "Duration": duration,
        "Units": units
    }
    requests.post("HTTP://" + ip + "/api/head", json=parameters)

move_head(0,0,0)