import RPi_I2C_driver
from time import *

lcd = RPi_I2C_driver.lcd(0x27)

while True:
    lcd.setCursor(0, 0)

    for thisChar in range(10):
        lcd.print(thisChar)
        sleep(0.5)

    lcd.setCursor(16, 1)
    lcd.autoscroll()

    for thisChar in range(10):
        lcd.print(thisChar)
        sleep(0.5)

    lcd.noAutoscroll()
    lcd.clear()