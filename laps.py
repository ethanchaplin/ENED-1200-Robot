#!/usr/bin/env python3


from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B
import CalibratedConstants as calib


global tank_drive 
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

NUM_LAPS = 3
LAP_DISTANCE = 120

def LAPS(n):
    for i in range(0, n):
        tank_drive.on_for_rotations(50, 50, (calib.CM_TO_ROTATION * LAP_DISTANCE))
        tank_drive.on_for_rotations(-50, -50, (calib.CM_TO_ROTATION * LAP_DISTANCE))

LAPS(NUM_LAPS)


