from gpiozero import Button, LED
import time

inputKeys = 16
keyPressed = 0

SCL_PIN = LED(27)
SDO_PIN = Button(22, pull_up = False)

def getKey():
        global keyPressed
        button = 0
        keyState = 0
        time.sleep(0.05)

        for i in range(inputKeys):

                SCL_PIN.off()

                if not SDO_PIN.is_pressed:
                        keyState = i + 1

                SCL_PIN.on()
                
        if (keyState>0 and keyState!=keyPressed):
                button = keyState
                keyPressed = keyState
        else:
                keyPressed = keyState
        return (button)

while True:
    key = getKey()
    if(key > 0):
        print(key)