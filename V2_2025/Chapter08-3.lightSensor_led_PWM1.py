import RPi.GPIO as GPIO
import spidev
import time

LED_PIN = 19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

PWM_FREQ = 700
LED = GPIO.PWM(LED_PIN, PWM_FREQ)
LED.start(0)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1260870

def analog_read_3208(channel):
    r = spi.xfer2([4 | 2 |(channel>>2), (channel &3) << 6,0])    
    adc_out = ((r[1]&15) << 8) + r[2]
    return adc_out

def map(x, in_min, in_max, out_min, out_max):
    out_val = (((x - in_min) * (out_max - out_min)) / (in_max - in_min)) + out_min
    return out_val

try:    
    while True:
        reading = analog_read_3208(1)
        voltage = reading * 3.3 / 4096

        if voltage < 1.5:
            brightness = 100
            LED.ChangeDutyCycle(brightness)
        elif voltage < 3.0:
            brightness = map(voltage, 1.5, 3.0, 100, 0)
            LED.ChangeDutyCycle(brightness)
        else:
            brightness = 0
            LED.ChangeDutyCycle(brightness)

        print("MCP3208:  Reading=%d\tVoltage=%0.2f\tbright_Percent=%0.1f" % (reading, voltage, brightness)) 
        time.sleep(1)

finally:
    GPIO.cleanup()

