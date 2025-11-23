import RPi_I2C_driver
from time import *

eleLogo1 = [
    0b00111,
    0b01000,
    0b10000,
    0b10100,
    0b10100,
    0b10100,
    0b10111,
    0b10000
]

eleLogo2 = [
    0b11100,
    0b00010,
    0b00001,
    0b01001,
    0b10101,
    0b10101,
    0b01001,
    0b00001
]
eleLogo3 = [
    0b01000,
    0b10101,
    0b10101,
    0b10101,
    0b10010,
    0b10000,
    0b01000,
    0b00111
]

eleLogo4 = [
    0b00001,
    0b11101,
    0b11101,
    0b10001,
    0b11101,
    0b00001,
    0b00010,
    0b11100
]

lcd = RPi_I2C_driver.lcd(0x27)

lcd.cursor()

lcd.print("Hello")

sleep(1)

lcd.print("Python!!!", 0.3)

sleep(2)

lcd.clear()

lcd.noCursor()

lcd.print("Raspberry Pi ", 0.2)

lcd.setCursor(6,1)
lcd.print("by LUMI", 0.3)

lcd.createChar(0, eleLogo1)
lcd.createChar(1, eleLogo2)
lcd.createChar(2, eleLogo3)
lcd.createChar(3, eleLogo4)

lcd.setCursor(14,0)

lcd.write(0)
lcd.write(1)

lcd.setCursor(14,1)

lcd.write(2)
lcd.write(3)

sleep(2)
lcd.blink()
sleep(1)

while True:
    for i in range(2):
        lcd.scrollDisplayLeft()
        sleep(0.5)

    for i in range(4):
        lcd.scrollDisplayRight()
        sleep(0.5)

    for i in range(2):
        lcd.scrollDisplayLeft()
        sleep(0.5)
