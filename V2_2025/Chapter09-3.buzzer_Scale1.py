import RPi.GPIO as GPIO
import time

buzzer_PIN = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_PIN, GPIO.OUT)

PWM_DutyCycle = 50
pwm = GPIO.PWM(buzzer_PIN, 0.1)

PWM_FREQ = [ 261.6256, \
             293.6648, \
             329.6276, \
             349.2282, \
             391.9954, \
             440.0000, \
             493.8833, \
             523.2511 ]

try:
    for i in range(0,8):
        pwm.start(PWM_DutyCycle)
        pwm.ChangeFrequency(PWM_FREQ[i])
        time.sleep(1.0)
        pwm.stop()
        time.sleep(0.5)       

finally:
    GPIO.cleanup()