import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D19)
#dhtDevice = adafruit_dht.DHT22(board.D19)

while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity  
        
        print("Temperature: {}C, Humidity: {}%".format(temperature, humidity))
        
    except RuntimeError:
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)