import RPi.GPIO as GPIO
import time

inputKeys=16
keyPressed=0

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

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
SCL_PIN=27
SDO_PIN=22
buzzer_PIN = 12

GPIO.setup(SCL_PIN,GPIO.OUT)
GPIO.setup(SDO_PIN,GPIO.IN)
GPIO.setup(buzzer_PIN, GPIO.OUT)

PWM_DutyCycle = 50
pwm = GPIO.PWM(buzzer_PIN, 0.1)

def getKey():
        global keyPressed
        button=0
        keyState=0
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
                for i in range(inputKeys):                    
  
                    if key == i + 1:
                        pwm.start(PWM_DutyCycle)
                        pwm.ChangeFrequency(PWM_FREQ[i])
                        time.sleep(0.2)
                        pwm.stop()

finally:
    GPIO.cleanup()