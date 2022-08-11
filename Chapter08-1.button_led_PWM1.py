import RPi.GPIO as GPIO
import time

LED_PIN = 19
Button_PIN = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Button_PIN, GPIO.IN)

PWM_FREQ = 700
LED = GPIO.PWM(LED_PIN, PWM_FREQ)
LED.start(0)

try:
    while 1:
        if GPIO.input(Button_PIN) == True:

            for i in range(0, 100, 1):
                LED.ChangeDutyCycle(i)
                time.sleep(0.02)

            for i in range(0, 101, 1):
                LED.ChangeDutyCycle(100 - i)
                time.sleep(0.02) 

finally:
    GPIO.cleanup()

