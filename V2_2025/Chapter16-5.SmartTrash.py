import RPi.GPIO as GPIO
from hx711 import HX711
import pickle
import os
import time

GPIO_TRIGGER = 22
GPIO_ECHO = 27
servoPIN = 17 
SERVO_MAX_DUTY = 12
SERVO_MIN_DUTY = 2 
LED_PIN = 19 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
hx = HX711(dout_pin=20, pd_sck_pin=16)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW )

servo = GPIO.PWM(servoPIN, 50) 
servo.start(0)

swap_file_name = 'HX711_config.swp'
if os.path.isfile(swap_file_name):
    with open(swap_file_name, 'rb') as swap_file:
        hx = pickle.load(swap_file)

else:
    err = hx.zero()
        
    if err:
        raise ValueError('용기 무게를 읽지 못했습니다.')

    reading = hx.get_raw_data_mean()
    if reading:
        print('로드셀 Raw Data 평균값: ', reading)
    else:
        print('로드셀 Raw Data가 유효하지 않음', reading)

    input('무게를 알고 있는 물체를 올려놓고 Enter를 눌러주세요.\n')
    reading = hx.get_data_mean() 
    if reading:
        print('Offset 값을 제외한 Raw Data 평균값: ', reading)
        known_weight_grams = input(
            '올려놓은 물체의 무게(g)를 입력 후 Enter를 눌러주세요: ')
        try:
            value = float(known_weight_grams)
            print(value, 'grams')
        except ValueError:
            print('예상 무게: ',
                  known_weight_grams)

        ratio = reading / value
        hx.set_scale_ratio(ratio)
        print('Conversion ratio 설정 완료.\n')
    else:
        raise ValueError(
            '평균값 계산 오류. 읽은 값(reading): ',
            reading)

    print('Conversion ratio 값을 HX711_config.swp에 저장')
    with open(swap_file_name, 'wb') as swap_file:
        pickle.dump(hx, swap_file)
        swap_file.flush()
        os.fsync(swap_file.fileno())

print("코드를 멈출려면 'CTRL + C'를 눌러주세요.")

def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def setServoPos(degree):
    degree = min(degree, 180)
    degree = max(degree, 0)

    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
  
    print("Degree: {},\tDuty: {}".format(degree, duty))

    servo.ChangeDutyCycle(duty)

try:
    while True:
        weight = round(hx.get_weight_mean(20), 1)
        print('쓰레기 무게: ' ,max(weight,0), 'g')
        
        if weight > 300:
            print('LED blink')
            GPIO.output(LED_PIN, 1)
            time.sleep(0.5)
            GPIO.output(LED_PIN, 0)
            time.sleep(0.5)
        else:
            GPIO.output(LED_PIN, 0)            
                
        dist = distance()
        print ("측정된 거리 = %.1f cm" % dist)
        
        if dist < 50:
            print('쓰레이통 두껑 열림')
            setServoPos(120)
            time.sleep(3)
        else:
            setServoPos(0)

finally:
    servo.stop()
    GPIO.cleanup()