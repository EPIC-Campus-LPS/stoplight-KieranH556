import RPi.GPIO as GPIO
import time
RCpin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RCpin, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.output(RCpin, GPIO.LOW)
time.sleep(0.1)

def RCtime(RCpin):
	reading = 0
	GPIO.setup(RCpin, GPIO.IN)
	time.sleep(0.05)
	while (GPIO.input(RCpin) == GPIO.LOW):
		reading += 1
		if reading > 5000:
			break
	return(reading)

# Main Loop
try:
	dark_threshold = 400
	while True:
		reading = RCtime(RCpin)
		if reading > dark_threshold:
			print("On")
			GPIO.output(20, GPIO.HIGH)
			GPIO.output(21, GPIO.HIGH)
			GPIO.output(19, GPIO.HIGH)
		elif reading == 0:
			GPIO.output(20, GPIO.LOW)
			GPIO.output(21, GPIO.LOW)
			GPIO.output(19, GPIO.LOW)
			print("Off")
	#	if reading == 0:
	#		GPIO.setup(20, GPIO.OUT)
	#		print("On")
	#		continue
	#	else:
	#		break
	#	GPIO.output(20, GPIO.LOW)
	#	print("Off")
except KeyboardInterrupt:
	GPIO.cleanup()
