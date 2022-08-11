import RPi.GPIO as GPIO
import time

servoPIN = 17
SERVO_MAX_DUTY = 12
SERVO_MIN_DUTY = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

servo = GPIO.PWM(servoPIN, 50)
servo.start(0)

def setServoPos(degree):
    degree = min(degree, 180)
    degree = max(degree, 0)

    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
    print("Degree: {},\tDuty: {}".format(degree, duty))
    servo.ChangeDutyCycle(duty)

if __name__ == "__main__":

    setServoPos(0)
    time.sleep(0.5)

    setServoPos(90)
    time.sleep(0.5)

    setServoPos(180)
    time.sleep(0.5)

    setServoPos(0)
    time.sleep(0.5)

    servo.stop()

    GPIO.cleanup()
