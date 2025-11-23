import RPi.GPIO as GPIO
import time

Button_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pressed = True

try:
    while True:
        print(GPIO.input(Button_PIN))

        if GPIO.input(Button_PIN):
            if pressed:
                print("버튼 누름")                
                pressed = False
        else:
            pressed = True
        time.sleep(0.1)

finally:
    GPIO.cleanup()
