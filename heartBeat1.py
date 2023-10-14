#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

motor1pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1pin, GPIO.OUT)

pwm1 = GPIO.PWM(motor1pin, 50) # GPIO 17 for PWM with 50Hz

pwm1.start(0)


def SetAngle(angle, servoPIN, pwm):
	duty = angle / 18 + 2
	GPIO.output(servoPIN, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(servoPIN, False)
	pwm.ChangeDutyCycle(0)

try:

    while True:
                    
        SetAngle(90, motor1pin, pwm1)
        sleep(5)
        SetAngle(0, motor1pin, pwm1)


except KeyboardInterrupt:
    
    for x in range(10):
        SetAngle(90, motor1pin, pwm1)
        sleep(1)
        SetAngle(0, motor1pin, pwm1)
        
    SetAngle(90, motor1pin, pwm1)
    sleep(5)
    SetAngle(0, motor1pin, pwm1)

    SetAngle(90, motor1pin, pwm1)
    sleep(10)
    SetAngle(0, motor1pin, pwm1)

    SetAngle(90, motor1pin, pwm1)
    sleep(15)
    SetAngle(0, motor1pin, pwm1)

    pwm1.stop()
    
    GPIO.cleanup()
