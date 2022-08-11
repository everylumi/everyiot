from gpiozero import LEDBoard
import time

FND_PIN = LEDBoard(20,12,6,19,26,16,5,13,9,10,22,27)

digits = ((1,1,1,1,1,1,0,0),
          (0,1,1,0,0,0,0,0),
          (1,1,0,1,1,0,1,0),
          (1,1,1,1,0,0,1,0),
          (0,1,1,0,0,1,1,0),
          (1,0,1,1,0,1,1,0),
          (1,0,1,1,1,1,1,0),
          (1,1,1,0,0,1,0,0),
          (1,1,1,1,1,1,1,0),
          (1,1,1,1,0,1,1,0),
          (1,1,1,1,0,1,1,1))

def initialLED():
    for i in range(8, 12, 1):
        FND_PIN[i].value = 1
        
def displayLED(Com_PIN, Number):
    initialLED()
    FND_PIN[Com_PIN].value = 0

    for i in range(0, 8, 1):
        FND_PIN[i].value = digits[Number][i]
    time.sleep(0.003) 

while 1:   
    Number = 1004

    w = int(Number / 1000)
    x = int((Number % 1000) / 100)
    y = int((Number % 100) / 10)
    z = int(Number % 10) 

    displayLED(8, w)
    displayLED(9, x)
    displayLED(10, y)
    displayLED(11, z)