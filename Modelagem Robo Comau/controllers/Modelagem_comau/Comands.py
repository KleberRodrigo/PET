from controller import Robot , PositionSensor, Motor, Keyboard
import math as m
import time as t
import numpy as np

key = '0'
TIME_STEP = 32
robot = Robot()
joint = []
MAX_SPEED = 5.0
Position_joint = [0.0]*6
Sensor_position_joint = []
TIME_STEP = 32
motor = 0
step_motor = m.radians(1)
erro = 1e-5
position = 0

keyboard = Keyboard()
keyboard.enable(TIME_STEP)

for i in range(0,6):
    Sensor_position_joint[i].enable(TIME_STEP)

for i in range(0,6):
    joint[i].setVelocity(0.1 * MAX_SPEED)

class Teclado:
    def Read_key():
      return keyboard.getKey()


