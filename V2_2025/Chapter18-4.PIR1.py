import RPi.GPIO as GPIO
import time

PIR_PIN = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    while 1:
        if GPIO.input(PIR_PIN) == True:
            print('센서가 감지되었습니다.')
        else:
            print('센서가 해제되었습니다.')
        
        time.sleep(1)

finally:
    GPIO.cleanup()

