from gpiozero import PWMLED, MCP3208
import time

LED_PIN = 19
ADC = MCP3208(channel=1)
PWM_FREQ = 700
LED = PWMLED(LED_PIN, active_high=True, initial_value=0, frequency=PWM_FREQ)

def map(x, in_min, in_max, out_min, out_max):
    out_val = (((x - in_min) * (out_max - out_min)) / (in_max - in_min)) + out_min
    return out_val

while True:
    reading = ADC.value * 4096
    voltage = ADC.value * 3.3

    if voltage < 1.5:
        brightness = 1
        LED.value = brightness
    elif voltage < 3.0:
        brightness = map(voltage, 1.5, 3.0, 1.0, 0)
        LED.value = brightness
    else:
        brightness = 0
        LED.value = brightness
        
    print("MCP3208:  Reading=%d\tVoltage=%0.2f\tbright_Percent=%0.1f" % (reading, voltage, brightness*100)) 
    time.sleep(1)
