#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

led = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)


GPIO.output(led, GPIO.HIGH)
time.sleep(8)
GPIO.output(led, GPIO.LOW)

GPIO.cleanup()
