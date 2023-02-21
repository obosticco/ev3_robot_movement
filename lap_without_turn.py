#!/usr/bin/env python3
from math import pi
from ev3dev2.motor import MoveTank, LargeMotor
from ev3dev2.sensor.lego import GyroSensor

tank_drive = MoveTank(left_motor_port="A", right_motor_port="D")
gyro = GyroSensor(address="2")
laps = 3   # int(input("Enter the number of laps: "))
length = 120    # float(input("Enter the length: "))

rotations = length / (4.07 * pi)  # 4.83 cm

for i in range(laps):
    tank_drive.on_for_rotations(35, 35, rotations)
    tank_drive.on_for_rotations(-35, -35, rotations)
