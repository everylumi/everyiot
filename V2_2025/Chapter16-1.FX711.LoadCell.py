import RPi.GPIO as GPIO
from hx711 import HX711
import pickle
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

hx = HX711(dout_pin=20, pd_sck_pin=16)

try:
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

    print("무게 측정을 멈출려면 'CTRL + C'를 눌러주세요.")
    input('Enter를 눌러서 무게 측정 시작!\n')
    while True:
        weight = round(hx.get_weight_mean(20), 1)
        print(max(weight,0), 'g')

finally:
    GPIO.cleanup()