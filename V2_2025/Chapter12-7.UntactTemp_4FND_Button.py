from smbus2 import SMBus
from mlx90614 import MLX90614
import RPi.GPIO as GPIO
import tm1637

Button_PIN = 21
CLK_PIN = 5
DIO_PIN = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_PIN, GPIO.IN)
tm = tm1637.TM1637(clk=CLK_PIN, dio=DIO_PIN)

def get_obj_temperature():
    bus = SMBus(1)
    sensor = MLX90614(bus, address=0x5A)  
    print('Ambient Temperature:\t{}'.format(sensor.get_amb_temp()))
    print('Object Temperature:\t{}\n'.format(sensor.get_obj_temp()))
    return sensor.get_obj_temp()

try:
    while 1:
        if GPIO.input(Button_PIN) == True:
            Number = round(get_obj_temperature(), 2)
            Number1 = int(Number // 1)
            Number2 = int((Number - Number1)*100)
            tm.numbers(Number1, Number2)

finally:
    GPIO.cleanup()
