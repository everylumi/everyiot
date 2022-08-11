import RPi.GPIO as GPIO

Button_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING)
        print("버튼 누름")

finally:
    GPIO.cleanup()
