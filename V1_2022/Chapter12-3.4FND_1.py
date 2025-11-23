import RPi.GPIO as GPIO
import time

FND_PIN = [20,12,6,19,26,16,5,13]
Com_PIN = [9,10,22,27]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in FND_PIN:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
for i in Com_PIN:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

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

def initialLED():
    for i in Com_PIN:
        GPIO.output(i, 1)
        
def displayLED(Com_PIN, Number):
    initialLED()
    GPIO.output(Com_PIN, 0)

    for i in range(0, 8, 1):
        GPIO.output(FND_PIN[i], digits[Number][i]) 
    time.sleep(0.003) 

try:
    while 1:
        Number = 1004

        w = int(Number / 1000)
        x = int((Number % 1000) / 100)
        y = int((Number % 100) / 10)
        z = int(Number % 10) 
                        
        displayLED(Com_PIN[0], w)
        displayLED(Com_PIN[1], x)
        displayLED(Com_PIN[2], y)
        displayLED(Com_PIN[3], z)        
         
finally:
    GPIO.cleanup()

