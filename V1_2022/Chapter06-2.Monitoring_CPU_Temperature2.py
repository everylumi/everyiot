import os
import time

def measure_temp():
        temp = os.popen('cat /sys/class/thermal/thermal_zone0/temp').read()
        return (int(temp)/1000)

while True:
        print(measure_temp())
        time.sleep(1)