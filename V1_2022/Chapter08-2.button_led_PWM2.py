from gpiozero import PWMLED, Button
import time

LED_PIN = 19
button = Button(21, pull_up = False)
PWM_FREQ = 700
LED = PWMLED(LED_PIN, active_high=True, initial_value=0, frequency=PWM_FREQ)

while True:
    if button.is_pressed:
        LED.pulse(fade_in_time=1, fade_out_time=1, n=1)
