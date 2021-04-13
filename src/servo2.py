import RPi.GPIO as GPIO
import time
import os

servo1 = 32
servo2 = 33

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo1,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)

# so for 50hz, one frequency is 20ms
# duty cycle 2 -> 0 degree
# duty cycle 12 -> 180 degree
# duty cylce 6 -> 90 degree

p1=GPIO.PWM(servo1,50)# 50hz frequency
p2=GPIO.PWM(servo2,50)

p1.start(0)
time.sleep(1)
p2.start(0)
time.sleep(1)

while True:
	for j in range(2,8,1):
    		p1.ChangeDutyCycle(j)
    		time.sleep(0.1)

	for j in range(8,2,-1):
    		p1.ChangeDutyCycle(j)
    		time.sleep(0.1)

	time.sleep(1)

	for j in range(2,8,1):
    		p2.ChangeDutyCycle(j)
    		time.sleep(0.1)

	for j in range(8,2,-1):
    		p2.ChangeDutyCycle(j)
    		time.sleep(0.1)

	time.sleep(60)


GPIO.cleanup()
