import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1260870

def analog_read_3208(channel):
    r = spi.xfer2([4 | 2 |(channel>>2), (channel &3) << 6,0])    
    adc_out = ((r[1]&15) << 8) + r[2]
    return adc_out

while True:
    reading = analog_read_3208(1)
    voltage = reading * 3.3 / 4096

    print("MCP3208: Reading=%d\tVoltage=%f" % (reading, voltage)) 
    time.sleep(1)

