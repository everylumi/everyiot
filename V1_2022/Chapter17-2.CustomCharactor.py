import RPi_I2C_driver
from time import *

heart = [
    0b00000,
    0b01010,
    0b11111,
    0b11111,
    0b11111,
    0b01110,
    0b00100,
    0b00000
]

smiley = [ 
    0b00000,
    0b00000,
    0b01010,
    0b00000,
    0b00000,
    0b10001,
    0b01110,
    0b00000
]

frownie = [
    0b00000,
    0b00000,
    0b01010,
    0b00000,
    0b00000,
    0b00000,
    0b01110,
    0b10001
]

armsDown = [
    0b00100,
    0b01010,
    0b00100,
    0b00100,
    0b01110,
    0b10101,
    0b00100,
    0b01010
]

armsUp = [
    0b00100,
    0b01010,
    0b00100,
    0b10101,
    0b01110,
    0b00100,
    0b00100,
    0b01010
]

lcd = RPi_I2C_driver.lcd(0x27)

lcd.createChar(0, heart)
lcd.createChar(1, smiley)
lcd.createChar(2, frownie)
lcd.createChar(3, armsDown)
lcd.createChar(4, armsUp)

lcd.setCursor(0, 0)

lcd.print("I ")
lcd.write(0)
lcd.print(" Ras Pi! ")
lcd.write(1)

while True:
    lcd.setCursor(4, 1)
    lcd.write(3)
    sleep(0.3)

    lcd.setCursor(4, 1)
    lcd.write(4)
    sleep(0.3)