import pickle
import RPi.GPIO as GPIO
import time
import os

servo1 = 18
servo2 = 22

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo1,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)

# so for 50hz, one frequency is 20ms
# duty cycle 2 -> 0 degree
# duty cycle 12 -> 180 degree
# duty cylce 6 -> 90 degree

p1=GPIO.PWM(servo1,50)# 50hz frequency
p2=GPIO.PWM(servo2,50)

with open(os.path.dirname(os.path.abspath(__file__)) + '/ldc','rb') as f:
    i = pickle.load(f)

p1.start(i)
time.sleep(1)
p2.start(i)
time.sleep(1)


""" p.ChangeDutyCycle(4)
time.sleep(0.5)
p.ChangeDutyCycle(6.5)
time.sleep(0.5)
p.ChangeDutyCycle(4)
time.sleep(0.5)
p.ChangeDutyCycle(2)
time.sleep(0.5) """

if i < 4:
  for j in range(2,8,1):
    p1.ChangeDutyCycle(j)
    time.sleep(0.07)

  time.sleep(0.9)

  for j in range(2,8,1):
    p2.ChangeDutyCycle(j)
    time.sleep(0.07)

  with open(os.path.dirname(os.path.abspath(__file__)) + '/ldc','wb') as f:
    pickle.dump(j,f)

else:
  for j in range(7,1,-1):
    p1.ChangeDutyCycle(j)
    time.sleep(0.07)

  time.sleep(0.9)

  for j in range(7,1,-1):
    p2.ChangeDutyCycle(j)
    time.sleep(0.07)

  with open(os.path.dirname(os.path.abspath(__file__)) + '/ldc','wb') as f:
    pickle.dump(j,f)

GPIO.cleanup()
    
