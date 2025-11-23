import RPi.GPIO as GPIO

Relay_PIN = 24
Button_PIN = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Relay_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Button_PIN, GPIO.IN)

try:
    while 1:
        if GPIO.input(Button_PIN) == True:
            GPIO.output(Relay_PIN, 1)
        else:
            GPIO.output(Relay_PIN, 0)

finally:
    GPIO.cleanup()

