from controller import Robot , PositionSensor, Motor, Keyboard
from Cinematica_inversa import *
import time as t
import numpy as np

robot = Robot()
joint = []
MAX_SPEED = 5.0
Position_joint = [0.0]*6
Sensor_position_joint = []
TIME_STEP = 32
key = '0'
motor = 0
step_motor = np.radians(1)
erro = 1e-5
position = 0

MCD = [
    [0, 0, 1, 800],
    [0, 1, 0, 0],
    [-1, 0, 0, 300],
    [0, 0, 0, 1]
]

joint.append(robot.getDevice('motor1'))
joint.append(robot.getDevice('motor2'))
joint.append(robot.getDevice('motor3'))
joint.append(robot.getDevice('motor4'))
joint.append(robot.getDevice('motor5'))
joint.append(robot.getDevice('motor6'))

Sensor_position_joint.append(robot.getDevice("position1"))
Sensor_position_joint.append(robot.getDevice("position2"))
Sensor_position_joint.append(robot.getDevice("position3"))
Sensor_position_joint.append(robot.getDevice("position4"))
Sensor_position_joint.append(robot.getDevice("position5"))
Sensor_position_joint.append(robot.getDevice("position6"))

keyboard = Keyboard()
keyboard.enable(TIME_STEP)


for i in range(0,6):
    Sensor_position_joint[i].enable(TIME_STEP)

for i in range(0,6):
    joint[i].setVelocity(0.1 * MAX_SPEED)


while robot.step(TIME_STEP) != -1:
    key = keyboard.getKey()
    #print(key)
    if (key >= 49) and (key<=54): #Definição do motor
        if key == 49:
            print("Junta 1")
            motor = 1
        elif key == 50:
            print("Junta 2")
            motor = 2
        elif key == 51:
            print("Junta 3")
            motor = 3
        elif key == 52:
            print("Junta 4")
            motor = 4
        elif key == 53:
            print("Junta 5")
            motor = 5 
        elif key == 54:
            print("Junta 6")
            motor = 6
        
    #Motores a partir do 2 sentido positivo        
    if key == 315: #Press key "up" 
            Position_joint[motor-1] = Sensor_position_joint[motor-1].getValue() + step_motor
            joint[motor-1].setPosition(Position_joint[motor-1])
            print("Rotacionando motor ",motor,"\nPosição Angular:",round(np.degrees(Position_joint[motor-1]),3),"º")
        
    #Motores a partir do 2 sentido negativo        
    if key == 317: #key down
            Position_joint[motor-1] = Sensor_position_joint[motor-1].getValue() - step_motor
            joint[motor-1].setPosition(Position_joint[motor-1])
            print("Rotacionando motor ",motor,"\nPosição Angular:",round(np.degrees(Position_joint[motor-1]),3),"º")
            
    if key == 86:
        step_motor = round((np.radians(float( input("Digite um valor em graus para step: ")))),3)

    if key == 73:
        robot.step(500)
        Position_joint = getAngles(MCD)
        for i in range(0,6):
            joint[i].setPosition(Position_joint[i])
        for i in range(0,6):
            print("Theta",i,":",round(np.degrees(Position_joint[i]),3))
    