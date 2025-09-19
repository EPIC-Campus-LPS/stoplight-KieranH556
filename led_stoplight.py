# Imports Libraries and sets configurations to operate
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Turns on and off the green light
GPIO.setup(21,GPIO.OUT)
print("Green Light On")
GPIO.output(21,GPIO.HIGH)
time.sleep(5)
GPIO.output(21,GPIO.LOW)
# Turns on and off the yellow light
GPIO.setup(18,GPIO.OUT)
print("Yellow Light On")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
# Turns on and off the red light 
GPIO.setup(19,GPIO.OUT)
print("Red Light On")   
GPIO.output(19,GPIO.HIGH)
time.sleep(4)
GPIO.output(19,GPIO.LOW)
