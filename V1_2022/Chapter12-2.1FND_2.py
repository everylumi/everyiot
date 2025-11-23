from gpiozero import LEDBoard, Button
import time

FND_PIN = LEDBoard(12,25,13,19,26,16,20,6)
button = Button(21, pull_up = False)

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

while 1:
    if button.is_pressed:
        for j in range(0, 11, 1):
            for i in range(0, 8, 1):
                FND_PIN[i].value = digits[j][i]
            time.sleep(0.5)


