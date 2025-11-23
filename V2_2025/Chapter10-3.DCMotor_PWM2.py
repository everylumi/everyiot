from gpiozero import Motor, Button
import time

Button_PIN = 21
A1A_PIN = 23
A1B_PIN = 24

motor = Motor(A1A_PIN, A1B_PIN)
button = Button(21, pull_up = False)

motor.stop()

while 1:
    if button.is_pressed:
        print('Power On')

        for i in range(50, 100, 1):
            print(i)
            motor.forward(i/100)
            time.sleep(0.1)
        motor.stop()
            
        time.sleep(1.2)
                
        for i in range(50, 100, 1):
            print(i)
            motor.backward(i/100)
            time.sleep(0.1)
        motor.stop()


