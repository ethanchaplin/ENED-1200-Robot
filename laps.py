#!/usr/bin/env python3


from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor
import os
import CalibratedConstants as calib




global tank_drive
global gyro 
gyro = GyroSensor(address="ev3-ports:in4")
ultra = UltrasonicSensor(address="ev3-ports:in3")

gyro.mode = GyroSensor.MODE_GYRO_ANG

ultra.mode = UltrasonicSensor.MODE_US_DIST_IN


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

NUM_LAPS = 3
LAP_DISTANCE = 120

def DRIVE(inches, dir):
    if (dir == 0):
       tank_drive.on_for_rotations(calib.POWER, calib.POWER,  float(inches) / calib.INCHES_TO_ROTATION)
    else:
        tank_drive.on_for_rotations(-calib.POWER, -calib.POWER, inches / calib.INCHES_TO_ROTATION) 

def ANGLE_CALIB():
    gyro.reset()
    tank_drive.on_for_rotations(-calib.POWER, calib.POWER, 1)
    
    calib.DEGREES_PER_ROTATION = float(gyro.angle)

    tank_drive.on_for_rotations(calib.POWER, -calib.POWER, 1)

def DISTANCE_CALIB():
    before = float(ultra.distance_inches)
    tank_drive.on_for_rotations(calib.POWER, calib.POWER, 1)
    after = float(ultra.distance_inches)

    calib.INCHES_TO_ROTATION = float((abs(after - before)))

    tank_drive.on_for_rotations(-calib.POWER, -calib.POWER, 1)

def SPIN(deg, dir):
   
    if(dir == 0):
    
        tank_drive.on_for_rotations(-calib.POWER, calib.POWER, float(deg) / calib.DEGREES_PER_ROTATION)
    else:
        tank_drive.on_for_rotations(calib.POWER, -calib.POWER, float(deg) / calib.DEGREES_PER_ROTATION)
    


gyro.reset()
print(gyro.angle)
ANGLE_CALIB()
DISTANCE_CALIB()

DRIVE(1, 0)
SPIN(180, 0)
DRIVE(1, 0)
SPIN(180, 0)
print(gyro.angle)

