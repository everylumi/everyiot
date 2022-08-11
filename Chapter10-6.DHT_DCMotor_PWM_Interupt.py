import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time

Button_PIN = 21
A1A_PIN = 23
A1B_PIN = 24
DHT_PIN = 19

pressed = False

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

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(A1A_PIN, GPIO.OUT)
GPIO.setup(A1B_PIN, GPIO.OUT)
GPIO.setup(Button_PIN, GPIO.IN)
GPIO.add_event_detect(Button_PIN, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=10)

PWM_FREQ = 50
A1A = GPIO.PWM(A1A_PIN, PWM_FREQ)
A1B = GPIO.PWM(A1B_PIN, PWM_FREQ)

try:
    while 1:
        humidity,temperature = dht.read_retry(dht.DHT11, DHT_PIN)
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


