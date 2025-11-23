from gpiozero import Button, LED
import time

RowPin = (12, 16, 20, 21)
Keys = (('1', '2', '3', 'A'),\
        ('4', '5', '6', 'B'),\
        ('7', '8', '9', 'C'),\
        ('*', '0', '#', 'D'))
button1 = Button(25, pull_up = False)
button2 = Button(24, pull_up = False)
button3 = Button(23, pull_up = False)
button4 = Button(18, pull_up = False)

def readbutton(button,i ,j):
    if button.is_pressed:
        print(Keys[i][j])
        time.sleep(0.5)

while True:
    for i in range(4):
        button_out = LED(RowPin[i])
        button_out.on()

        readbutton(button1, i, 0)
        readbutton(button2, i, 1)
        readbutton(button3, i, 2)
        readbutton(button4, i, 3) 

        button_out.off()
     




