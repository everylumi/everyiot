from gpiozero import LED, Button
import time

led = LED(19)
button = Button(21, pull_up = False)
state = 0
var = 0
old_var = 0

while True:
    var = button.value

    if ((var == 1) and (old_var == 0)):
        state = 1 - state

        time.sleep(10 / 1000)
        
    old_var = var

    if state == 1:
        led.on()
    else:
        led.off()
