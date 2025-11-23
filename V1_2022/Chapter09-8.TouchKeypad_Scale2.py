from gpiozero import Button, LED, PWMLED
import time

inputKeys = 16
keyPressed = 0
PWM_DutyCycle = 0.5

PWM_FREQ = [ 174.6141, \
             195.9977, \
             220.0000, \
             246.9417, \
             261.6256, \
             293.6648, \
             329.6276, \
             349.2282, \
             391.9954, \
             440.0000, \
             493.8833, \
             523.2511, \
             587.3295, \
             659.2551, \
             698.4565, \
             783.9909 ]

SCL_PIN = LED(27)
SDO_PIN = Button(22, pull_up = False)
bz = PWMLED(12, active_high=True, initial_value=0)

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
        
        for i in range(inputKeys):                    
     
            if key == i + 1:
                bz.on()
                bz.value = PWM_DutyCycle
                bz.frequency = int(PWM_FREQ[i])
                time.sleep(0.2)
                bz.off()

