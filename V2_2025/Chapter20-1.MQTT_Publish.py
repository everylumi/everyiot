import RPi.GPIO as GPIO
import board
import adafruit_dht
import time
import paho.mqtt.client as mqtt

Button_PIN = 19
LED_PIN = 21
dhtDevice = adafruit_dht.DHT11(board.D26)
#dhtDevice = adafruit_dht.DHT22(board.D26)


pressed = False 

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("homenet/Sensor1/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect("192.168.219.139", 1883, 60)  #mqtt 서버 IP

mqttc.loop_start()

def button_pressed_callback(channel):
    global pressed
    
    pressed = 1 - pressed
    
    if pressed:
        print('버튼 On')
        GPIO.output(LED_PIN,GPIO.HIGH)
        mqttc.publish("homenet/Sensor1/LED", 'ON')

    else:
        print('버튼 Off')
        GPIO.output(LED_PIN,GPIO.LOW)
        mqttc.publish("homenet/Sensor1/LED", 'OFF')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Button_PIN, GPIO.IN)
GPIO.add_event_detect(Button_PIN, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=10)

try:
    while 1:
    
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity  
        print(temperature)

        mqttc.publish("homenet/Sensor1/temperature", temperature)
        mqttc.publish("homenet/Sensor1/humidity", humidity)
        time.sleep(0.5)
        
finally:
    mqttc.loop_stop()
    GPIO.cleanup()