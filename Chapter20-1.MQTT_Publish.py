import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time
import paho.mqtt.client as mqtt

Button_PIN = 19
LED_PIN = 21
DHT_PIN = 26

pressed = False

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("homenet/Sensor1/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.219.206", 1883, 60)

def button_pressed_callback(channel):
    global pressed

    pressed = 1 - pressed
    
    if pressed:
        print('버튼 On')
        GPIO.output(LED_PIN,GPIO.HIGH)

        client.publish("homenet/Sensor1/LED", 'ON')

    else:
        print('버튼 Off')
        GPIO.output(LED_PIN,GPIO.LOW)
        client.publish("homenet/Sensor1/LED", 'OFF')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Button_PIN, GPIO.IN)
GPIO.add_event_detect(Button_PIN, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=10)

try:
    while 1:
        humidity,temperature = dht.read_retry(dht.DHT11, DHT_PIN)
        print(temperature)
        client.publish("homenet/Sensor1/temperature", temperature)
        client.publish("homenet/Sensor1/humidity", humidity)

finally:
    GPIO.cleanup()