import RPi.GPIO as GPIO
import time

FND_PIN = [12,25,13,19,26,16,20,6]
Button_PIN = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in FND_PIN:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Button_PIN, GPIO.IN)

digits = ((1,1,1,1,1,1,0,0),
          (0,1,1,0,0,0,0,0),
          (1,1,0,1,1,0,1,0),
          (1,1,1,1,0,0,1,0),
          (0,1,1,0,0,1,1,0),
          (1,0,1,1,0,1,1,0),
          (1,0,1,1,1,1,1,0),
          (1,1,1,0,0,1,0,0),
          (1,1,1,1,1,1,1,0),
          (1,1,1,1,0,1,1,0),
          (1,1,1,1,0,1,1,1))

try:
    while 1:
        if GPIO.input(Button_PIN) == True:

            for j in range(0, 11, 1):
                for i in range(0, 8, 1):
                    GPIO.output(FND_PIN[i], digits[j][i]) 
                time.sleep(0.5)

finally:
    GPIO.cleanup()

