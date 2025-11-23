from gpiozero import LED, Button

Relay = LED(24)
button = Button(21, pull_up = False)

while True:
    if button.is_pressed:
        Relay.on()
    else:
        Relay.off()

