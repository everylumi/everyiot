from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=27, trigger=22, max_distance=4)

while True:
    dist = sensor.distance * 100
    print ("측정된 거리 = %.1f cm" % dist)
    sleep(1)
