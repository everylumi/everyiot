import RPi.GPIO as GPIO
import time

RowPin = (12, 16, 20, 21)
ColPin = (25, 24, 23, 18)
Keys = (('1', '2', '3', 'A'),\
        ('4', '5', '6', 'B'),\
        ('7', '8', '9', 'C'),\
        ('*', '0', '#', 'D'))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in RowPin:
    GPIO.setup(i, GPIO.OUT)   
for j in ColPin:
    GPIO.setup(j, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

try:
    while True:
        for i in range(4):
            GPIO.output(RowPin[i], GPIO.HIGH)
            
            for j in range(4):
                if GPIO.input(ColPin[j]) == 1:
                    print(Keys[i][j])
                    time.sleep(0.5)
       
            GPIO.output(RowPin[i], GPIO.LOW)            

finally:
    GPIO.cleanup()
