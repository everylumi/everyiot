import RPi.GPIO as GPIO
import time

inputKeys = 16
keyPressed = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
SCL_PIN = 27
SDO_PIN = 22

GPIO.setup(SCL_PIN,GPIO.OUT)
GPIO.setup(SDO_PIN,GPIO.IN)

def getKey():
        global keyPressed
        button = 0
        keyState = 0
        time.sleep(0.05)
        
        for i in range(inputKeys):
                GPIO.output(SCL_PIN, GPIO.LOW)
                
                if not GPIO.input(SDO_PIN):
                        keyState = i + 1
                
                GPIO.output(SCL_PIN, GPIO.HIGH)
                
        if (keyState>0 and keyState!=keyPressed):
                button = keyState
                keyPressed = keyState
        else:
                keyPressed = keyState
        return (button)

try:
    while True:
            key = getKey()
            if(key > 0):
                print(key)

finally:
    GPIO.cleanup()