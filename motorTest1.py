#!/usr/bin/env python

import RPi.GPIO as GPIO
#from mfrc522 import SimpleMFRC522
from time import sleep

motor1pin = 11
motor2pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1pin, GPIO.OUT)
GPIO.setup(motor2pin, GPIO.OUT)

pwm1 = GPIO.PWM(motor1pin, 50) # GPIO 17 for PWM with 50Hz
pwm2 = GPIO.PWM(motor2pin, 50) # GPIO 27 for PWM with 50Hz

pwm1.start(0)
pwm2.start(0)

#paintingA = '222767519619'
#paintingB = '632265873354'
#paintingC = '770543687608'

#reader = SimpleMFRC522()

def SetAngle(angle, servoPIN, pwm):
	duty = angle / 18 + 2
	GPIO.output(servoPIN, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(servoPIN, False)
	pwm.ChangeDutyCycle(0)

try:
   # id, text = reader.read()
    #rfidTag = str(id)
    
   # print(id)
  #  print(text)

  #  while rfidTag != paintingB:
       # id, text = reader.read()
       #rfidTag = str(id)
        
       # print(id)
       # print(text)
       # if rfidTag == paintingB:
      #      break
        
   # print("yes, B")
        
   # sleep(10)
        
   # while rfidTag != paintingC:
      #  id, text = reader.read()
      #  rfidTag = str(id)
        
      #  print(id)
      #  print(text)
      #  if rfidTag == paintingC:
      #      break
        
   # print("yes, c")
            
   # sleep(10)
    #while rfidTag != paintingA:
       # id, text = reader.read()
      #  rfidTag = str(id)
        
       # print(id)
      #  print(text)
      #  if rfidTag == paintingA:
       #     break    

            
    #print("yes, a")
                
    #sleep(3)
                
    SetAngle(90, motor1pin, pwm1)
    sleep(15)
    SetAngle(0, motor1pin, pwm1)

    print("puzzle 1 solved")
    print("please remove pictures")
    print("30 seconds")
    sleep(30)
    print("puzzle 2 start")
   
   # id, text = reader.read()
    #rfidTag = str(id)
    
    ## print(text)


   # while rfidTag != paintingA:
    #    id, text = reader.read()
      #  rfidTag = str(id)
        
       # print(id)
        #print(text)
        #if rfidTag == paintingA:
            #break    
                    
    #print("yes, a")
                    
    #sleep(10)
    
    #while rfidTag != paintingB:
       # id, text = reader.read()
       # rfidTag = str(id)
        
      #  print(id)
      #  print(text)
      #  if rfidTag == paintingB:
       #     break
        
   # print("yes, B")
        
    #sleep(10)

   # while rfidTag != paintingC:
       # id, text = reader.read()
       # rfidTag = str(id)
        
       # print(id)
       # print(text)
      # if rfidTag == paintingC:
         #   break
        
    #print("yes, c")
            
   # sleep(3)                        
                    
   # print("puzzle 2 solved")

    SetAngle(90, motor2pin, pwm2)
    sleep(15)
    SetAngle(0, motor2pin, pwm2) 


except KeyboardInterrupt:
  pwm1.stop()
  pwm2.stop()
  GPIO.cleanup()
