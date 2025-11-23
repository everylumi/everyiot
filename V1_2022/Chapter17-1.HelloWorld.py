import RPi_I2C_driver
from time import *

lcd = RPi_I2C_driver.lcd(0x27)
lcd.print("hello, world!")
time_sec = 0

while True:
    lcd.setCursor(0, 1)

    lcd.print(time_sec) 
    sleep(1)
    
    time_sec += 1