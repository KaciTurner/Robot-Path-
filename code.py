# Simple code to read a message from the Dabble App over the DSDTech HM-10 bluetooth module
# Author: Eric Z. Ayers <ericzundel@gmail.com>

"""CircuitPython Example of how to read data from the Dabble app"""
import binascii #binascii imports libraries that we need
import board
import busio
import digitalio
import time
import pwmio

from dabble import Dabble  #imports the libraries that we need
dabble = Dabble(board.GP0, board.GP1, debug=True)  #Attaches it to a gp and turns it on.
from adafruit_motor import motor

left_motor_forward = board.GP12
left_motor_backward = board.GP13
right_motor_forward = board.GP15
right_motor_backward = board.GP14
# Troubleshooting
#right_motor_forward = board.GP3
#right_motor_backward = board.GP2


pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)
pwm_Ra = pwmio.PWMOut(right_motor_forward, frequency=10000)
pwm_Rb = pwmio.PWMOut(right_motor_backward, frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)
Left_Motor_speed = 0
Right_Motor = motor.DCMotor(pwm_Ra, pwm_Rb)
Right_Motor_speed = 0

def Robot_forward():
    Left_Motor_speed = .7
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = .7
    Right_Motor.throttle = Right_Motor_speed

def Robot_backward():
    Left_Motor_speed = -.7
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -.7
    Right_Motor.throttle = Right_Motor_speed

def Robot_left():
    Left_Motor_speed = -.7
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = .7
    Right_Motor.throttle = Right_Motor_speed

def Robot_right():
    Left_Motor_speed = .7
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -.7
    Right_Motor.throttle = Right_Motor_speed

def Robot_stop():
    Left_Motor_speed = 0
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 0
    Right_Motor.throttle = Right_Motor_speed

while True:
    message = dabble.read_message()
    if (message != None):
        #print("Message: " + str(message))
        # Implement tank steering on a 2 wheeled robot
        if (message.up_arrow_pressed):
            print("Move both motors forward")
            Robot_forward()
        elif (message.down_arrow_pressed):
            print("Move both motors backward")
            Robot_backward()
        elif (message.right_arrow_pressed):
            print("Move left motor forward and right motor backward")
            Robot_right()
        elif (message.left_arrow_pressed):
            print("Move left motor backward and right motor forward")
            Robot_left()
        elif (message.no_direction_pressed):
            print("Stop both motors")
            Robot_stop()
        else:
            print("Something crazy happened with direction!")

