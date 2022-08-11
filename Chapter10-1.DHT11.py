import Adafruit_DHT as dht
import time

DHT_PIN = 19

while True:
    try:
        
        humidity,temperature = dht.read_retry(dht.DHT11, DHT_PIN)    #DHT11 사용 시 
        #humidity,temperature = dht.read_retry(dht.DHT22, DHT_PIN)   #DHT22 사용 시 
        time.sleep(10)
        
        print("Temperature: {}C, Humidity: {}%".format(temperature, humidity))
        
    except RuntimeError:
        pass
