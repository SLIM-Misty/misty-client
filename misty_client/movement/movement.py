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

"""Drives Misty forward or backward at a specific speed until cancelled.
When using the Drive command, it helps to understand how linear velocity (speed in a straight line) and angular velocity (speed and direction of rotation) work together:
Linear velocity (-100) and angular velocity (0) = driving straight backward at full speed.
Linear velocity (100) and angular velocity (0) = driving straight forward at full speed.
Linear velocity (0) and angular velocity (-100) = rotating clockwise at full speed.
Linear velocity (0) and angular velocity (100) = rotating counter-clockwise at full speed.
Linear velocity (non-zero) and angular velocity (non-zero) = Misty drives in a curve.
Endpoint: POST <robot-ip-address>/api/drive
Parameters
LinearVelocity (double) - A percent value that sets the speed for Misty when she drives in a straight line. Default value range is from -100 (full speed backward) to 100 (full speed forward).
AngularVelocity (double) - A percent value that sets the speed and direction of Misty's rotation. Default value range is from -100 (full speed rotation clockwise) to 100 (full speed rotation counter-clockwise). Note: For best results when using angular velocity, we encourage you to experiment with using small positive and negative values to observe the effect on Misty's movement.
{
  "LinearVelocity": 20,
  "AngularVelocity": 15,
}
JSON
Return Values
Result (boolean) - Returns true if there are no errors related to this command."""

def drive(lin_vel=50,ang_vel=50, vel_type='linear'):
    if vel_type is 'linear':
        parameters = {
            "LinearVelocity":lin_vel
        }
    elif vel_type is 'angular':
        parameters = {
            "AngularVelocity":ang_vel
        }
    requests.post("HTTP://" + ip + "/api/drive", json=parameters)

"""DriveTime
Drives Misty forward or backward at a set speed, with a given rotation, for a specified amount of time.
When using the DriveTime command, it helps to understand how linear velocity (speed in a straight line) and angular velocity (speed and direction of rotation) work together:
Linear velocity (-100) and angular velocity (0) = driving straight backward at full speed.
Linear velocity (100) and angular velocity (0) = driving straight forward at full speed.
Linear velocity (0) and angular velocity (-100) = rotating clockwise at full speed.
Linear velocity (0) and angular velocity (100) = rotating counter-clockwise at full speed.
Linear velocity (non-zero) and angular velocity (non-zero) = Misty drives in a curve.
Endpoint: POST <robot-ip-address>/api/drive/time
Parameters
LinearVelocity (double) - A percent value that sets the speed for Misty when she drives in a straight line. Default value range is from -100 (full speed backward) to 100 (full speed forward).
AngularVelocity (double) - A percent value that sets the speed and direction of Misty's rotation. Default value range is from -100 (full speed rotation clockwise) to 100 (full speed rotation counter-clockwise). Note: For best results when using angular velocity, we encourage you to experiment with using small positive and negative values to observe the effect on Misty's movement.
TimeMs (integer) - A value in milliseconds that specifies the duration of movement. Misty will not drive if you pass in a value of less than 100 for this parameter.
Degree (double) - (optional) The number of degrees to turn. Note: Supplying a Degree value recalculates linear velocity.
{
  "LinearVelocity": 1,
  "AngularVelocity": 4,
  "TimeMS": 500
}
JSON
Return Values
Result (boolean) - Returns true if there are no errors related to this command."""
def drive_time(lin_vel=50, ang_vel=50, vel_type='linear', degree=180, time_ms=500, time_type='time'):
    parameters = {}
    if vel_type is 'linear':
        parameters['LinearVelocity'] = lin_vel
    elif vel_type is 'angular':
        parameters['AngularVelocity'] = ang_vel

    if time_type is 'time':
        parameters['TimeMS'] = time_ms
    elif time_type is 'degree':
        parameters['Degree'] = degree

    requests.post("HTTP://" + ip + "/api/drive/time", json=parameters)







