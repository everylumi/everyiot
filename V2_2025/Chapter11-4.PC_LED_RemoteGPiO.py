'''
Date    : Jan-27, 2025
Book    : "라즈베리파이로 IoT 만들기"
Chapter : 11
 - 예제코드 4
 - Remote GPIO으로 LED 작동
'''

# 라이브러리 호출
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# GPIO 설정
factory = PiGPIOFactory(host='192.168.219.206')
led = LED(19, pin_factory=factory)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

