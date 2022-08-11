#!/usr/bin/env python3

import tm1637
from time import sleep

CLK_PIN = 5
DIO_PIN = 4
DELAY = 0.5

tm = tm1637.TM1637(clk=CLK_PIN, dio=DIO_PIN)

tm.write([0, 0, 0, 0])
tm.show('    ')
sleep(DELAY)

tm.show('1004')
sleep(DELAY)

tm.brightness(0)
sleep(DELAY)

tm.brightness(7)
sleep(DELAY)

tm.number(205)
sleep(DELAY)

tm.numbers(12, 59)
tm.show('1259', True)
sleep(DELAY)