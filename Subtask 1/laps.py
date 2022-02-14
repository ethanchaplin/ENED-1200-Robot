#!/usr/bin/env python3


from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B


global tank_drive 
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

NUM_LAPS = 2
LAP_DISTANCE = 12.7 #calibrate this metric.
INCHES_TO_ROTATION = (1/5.25) #this too.
CM_TO_ROTATION = INCHES_TO_ROTATION * (1/2.54)
POWER = 50


def LAPS(n):
    for i in range(0, n):
        tank_drive.on_for_rotations(50, 50, (CM_TO_ROTATION * LAP_DISTANCE))
        tank_drive.on_for_rotations(-50, -50, (CM_TO_ROTATION * LAP_DISTANCE))

LAPS(NUM_LAPS)


