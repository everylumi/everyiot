from gpiozero import MCP3008
import time

ADC = MCP3008(channel=1)
while True :
    reading = ADC.value * 1024
    voltage = ADC.value * 3.3
    
    print("MCP3008: Reading=%d\tVoltage=%f" % (reading, voltage)) 
    time.sleep(1)
