from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

Relay_PIN = 24

factory = PiGPIOFactory(host='192.168.219.206')
red = LED(Relay_PIN,pin_factory=factory)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)

