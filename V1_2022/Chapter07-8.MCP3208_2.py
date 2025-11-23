from gpiozero import MCP3208
import time

ADC = MCP3208(channel=1)
while True :
    reading = ADC.value * 4096
    voltage = ADC.value * 3.3
    
    print("MCP3208: Reading=%d\tVoltage=%f" % (reading, voltage)) 
    time.sleep(1)

