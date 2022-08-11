import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1936957

def analog_read_3008(channel):
    r = spi.xfer2([1, (8+channel) << 4,0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out

while True:
    reading = analog_read_3008(1)
    voltage = reading * 3.3 / 1024

    print("MCP3008: Reading=%d\tVoltage=%f" % (reading, voltage)) 
    time.sleep(1)

