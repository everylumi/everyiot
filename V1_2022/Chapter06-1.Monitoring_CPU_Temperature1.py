import os
import time

def measure_temp():
        temperature= os.popen('vcgencmd measure_temp').readline()
        return (temperature.replace('temp=', ''))

while True:
        print(measure_temp(), end='')
        time.sleep(1)