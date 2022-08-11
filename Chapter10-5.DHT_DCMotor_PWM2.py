from gpiozero import Motor, Button
import Adafruit_DHT as dht
import time

Button_PIN = 21
A1A_PIN = 23
A1B_PIN = 24
DHT_PIN = 19

state = 0
var = 0
old_var = 0

motor = Motor(A1A_PIN, A1B_PIN)
button = Button(21, pull_up = False)

while 1:
    humidity,temperature = dht.read_retry(dht.DHT11, DHT_PIN)
    print(temperature)

    if temperature > 30:
        print('온도 30도씨 조과')
        motor.forward(1)
    elif temperature > 27:
        print('온도 27도씨 조과')
        motor.forward(0.7)
    else:
        var = button.value

        if ((var == 1) and (old_var == 0)):
            state = 1 - state
            time.sleep(10 / 1000)
            
        old_var = var

        if state == 1:
            print('버튼 On')
            motor.forward(0.7)
        else:
            print('버튼 Off')
            motor.stop() 

