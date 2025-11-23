'''
Date    : Jan-27, 2025
Book    : "라즈베리파이로 IoT 만들기"
Chapter : 11
 - 예제코드 5
 - Remote GPIO으로 2대의 라즈베리파이 LED 작동
'''

# 라이브러리 호출
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# GPIO 설정
factory1 = PiGPIOFactory(host='192.168.219.205')
factory2 = PiGPIOFactory(host='192.168.219.206')
led_1 = LED(19, pin_factory=factory1)
led_2 = LED(19, pin_factory=factory2)

while True:
    led_1.on()
    led_2.off()
    sleep(1)
    led_1.off()
    led_2.on()
    sleep(1)

