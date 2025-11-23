import RPi.GPIO as GPIO
import time

Button_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pressed = False

try:
    while True:
        print(GPIO.input(Button_PIN))

        if not GPIO.input(Button_PIN):
            if not pressed:
                print("버튼 누름")                
                pressed = True
        else:
            pressed = False
        time.sleep(0.1)

finally:
    GPIO.cleanup()
