from gpiozero import MCP3208, LED
import time

led = LED(19)
ADC = MCP3208(channel=1)

while True :
    reading = ADC.value * 4096
    voltage = ADC.value * 3.3
    
    print("MCP3208: Reading=%d\tVoltage=%f" % (reading, voltage)) 
    time.sleep(1)

    if voltage < 1.5:
        led.on()
    else:
        led.off()

