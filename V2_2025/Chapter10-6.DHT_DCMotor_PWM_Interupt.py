import RPi.GPIO as GPIO
import board
import adafruit_dht
import time

Button_PIN = 21
A1A_PIN = 23 
A1B_PIN = 24

pressed = 0 

def button_pressed_callback(channel):
    global pressed
    
    pressed = 1 - pressed
    
    if pressed:
        print('버튼 On')
        A1A.start(0)                
        A1A.ChangeDutyCycle(70)
    else:
        print('버튼 Off')
        A1A.stop() 

dhtDevice = adafruit_dht.DHT11(board.D19)
#dhtDevice = adafruit_dht.DHT22(board.D19)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(A1A_PIN, GPIO.OUT, initial=0)
GPIO.setup(A1B_PIN, GPIO.OUT, initial=0)
GPIO.setup(Button_PIN, GPIO.IN)
GPIO.add_event_detect(Button_PIN, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=10)

PWM_FREQ = 50 
A1A = GPIO.PWM(A1A_PIN, PWM_FREQ)
A1B = GPIO.PWM(A1B_PIN, PWM_FREQ)

A1A.stop()

try:
    while 1:    
        temperature = dhtDevice.temperature
        print(temperature)
        
        if temperature > 30:
            print('온도 30도씨 조과')
            A1A.start(0)                
            A1A.ChangeDutyCycle(100)

        elif temperature > 27:
            print('온도 27도씨 조과')
            A1A.start(0)                
            A1A.ChangeDutyCycle(70)

        elif pressed == 0:
            A1A.stop()

finally:
    GPIO.cleanup()
    dhtDevice.exit()


