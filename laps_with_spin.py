#!/usr/bin/env python3


from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B


global tank_drive 
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

NUM_LAPS = 2
LAP_DISTANCE = 5
INCHES_TO_ROTATION = (1/5.25)
CM_TO_ROTATION = INCHES_TO_ROTATION * (1/2.54)
POWER = 50
DEGREES_PER_ROTATION = 164



def TURN(n):
    tank_drive.on_for_rotations(POWER, -POWER, n * (1 / DEGREES_PER_ROTATION))

def LAPS(n):
    for i in range(0, n):
        tank_drive.on_for_rotations(POWER, POWER, LAP_DISTANCE * INCHES_TO_ROTATION)
        TURN(180)

LAPS(1)
TURN(180)

