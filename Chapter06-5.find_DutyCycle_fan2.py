import RPi.GPIO as GPIO
import time
import sys

FAN_PIN = 14
PWM_FREQ = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)

fan=GPIO.PWM(FAN_PIN, PWM_FREQ)
fan.start(0)

try:
    while 1:
        fanSpeed=float(input("Fan Speed: "))
        fan.ChangeDutyCycle(fanSpeed)

except(KeyboardInterrupt):
    print("Fan ctrl interrupted by keyboard")
    GPIO.cleanup()
    sys.exit()
