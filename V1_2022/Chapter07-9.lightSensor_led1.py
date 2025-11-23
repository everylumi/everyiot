import RPi.GPIO as GPIO
import spidev
import time

LED_PIN = 19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1260870

def analog_read_3208(channel):
    r = spi.xfer2([4 | 2 |(channel>>2), (channel &3) << 6,0])    
    adc_out = ((r[1]&15) << 8) + r[2]
    return adc_out

try:    
    while True:
        reading = analog_read_3208(1)
        voltage = reading * 3.3 / 4096

        print("MCP3208: Reading=%d\tVoltage=%f" % (reading, voltage)) 
        time.sleep(1)

        if voltage < 1.5:
            GPIO.output(LED_PIN,GPIO.HIGH)
            print("LED ON")
        else :
            GPIO.output(LED_PIN,GPIO.LOW)
            print("LED OFF")

finally:
    GPIO.cleanup()
