import RPi.GPIO as GPIO
import time

Button_PIN = 16

def button_pressed_callback(channel):
    print("버튼 누름")

GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(Button_PIN, GPIO.FALLING,
                      callback=button_pressed_callback, bouncetime=100)

try:
    while True:
        print(GPIO.input(Button_PIN))
        time.sleep(10)

finally:
    GPIO.cleanup()


