import RPi.GPIO as GPIO
import time

LED_PIN = 19
Button_PIN = 21
state = 0
var = 0
old_var = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Button_PIN, GPIO.IN)

try:
    while 1:
        var = GPIO.input(Button_PIN)

        if ((var == 1) and (old_var == 0)):
            state = 1 - state

            time.sleep(10 / 1000)
        
        old_var = var
        
        if state == 1:
            GPIO.output(LED_PIN, 1)
        else:
            GPIO.output(LED_PIN, 0)           

finally:
    GPIO.cleanup()


