import RPi.GPIO as GPIO
import time
from gpiozero import Button
from gpiozero import Button
from signal import pause
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
last_press_time  = 0
# Function called when the sensor is touched 
def touched():
# Debunce to prevent multiple instances running in one press.
	global last_press_time
	current_time = time.time()
	if (current_time - last_press_time) > 0.2:
 # Print a message indicating the sensor is touched
		print("Touched!")
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
# Function called when the sensor is not touched
def not_touched():
    # Print a message indicating the sensor is not touched
	print("Not touched!")

# Initialize a Button object for the touch sensor
# pull_up=None: disable internal pull-up/pull-down resistors
# active_state=True: high voltage is considered the active state
touch_sensor = Button(20, pull_up=None, active_state=True,)
# Assign functions to sensor events
touch_sensor.when_pressed = touched
touch_sensor.when_released = not_touched

pause()  # Keep the program running to detect touch events
