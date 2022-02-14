#!/usr/bin/env python3


from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B
import CalibratedConstants as calib

global tank_drive 
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)




def TURN(n):
    tank_drive.on_for_rotations(calib.POWER, -calib.POWER, n * (1 / calib.DEGREES_PER_ROTATION))

def LAPS(n):
    for i in range(0, n):
        tank_drive.on_for_rotations(calib.POWER, calib.POWER, calib.LAP_DISTANCE * calib.INCHES_TO_ROTATION)
        TURN(180)

LAPS(1)
TURN(180)

