import RPi.GPIO as GPIO
import time
import sys

from picamera2 import Picamera2

import smtplib
from email.message import EmailMessage

import os
import shutil
import mimetypes
from datetime import datetime
from pathlib import Path 

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') 
logging.debug('Start of Program')

directory = '/home/pi/Desktop'

def now_time():
    now = datetime.now()
    global dt_string
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

def sending_mail():
    now_time()

    msg = EmailMessage()
    msg['Subject'] = '감시카메라에서 사진 송부' 
    msg['From'] = '네이버아이디@naver.com' 
    msg['To'] = '받을사람 메일주소' 
    msg.set_content('''
    안녕하세요.
    감시카메라에서 {}에 촬영한 사진 송부합니다.
    '''.format(dt_string))

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if not os.path.isfile(path):
            continue

        ctype, encoding = mimetypes.guess_type(path)

        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'

        maintype, subtype = ctype.split('/', 1)

        with open(path, 'rb') as fp:
            msg.add_attachment(fp.read(),
                               maintype=maintype,
                               subtype=subtype,
                               filename=filename)

    smtp = smtplib.SMTP_SSL('smtp.naver.com', 465)
    smtp.ehlo()

    smtp.login('네이버아이디', '비밀번호')
    smtp.send_message(msg)
    smtp.quit()
    logging.info('사진이 전송되었습니다.')
    move_photos()

def move_photos():

    p = Path(directory + '/Photos')
    p.mkdir(exist_ok=True)
    directory_photos = directory + '/Photos'

    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            logging.info(filename)
            shutil.move(directory + '/' + filename, directory_photos + '/' + filename)
    logging.info('사진이 저장되었습니다.')
 

PIR_PIN = 21

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
    
i = 0 
    
picam2 = Picamera2()
picam2.start()
logging.info('감시시스템이 작동 되었습니다.')

try:
    while True:
        if GPIO.input(PIR_PIN) == True:
            logging.info('센서가 감지되었습니다.')
            now_time()
            picam2.capture_file(directory + '/{}.jpg'.format(dt_string))
            time.sleep(1)
            i = i + 1
            logging.info('{}장 촬영'.format(i))
                
            if i == 5:
                sending_mail()
                i = 0                    
        else:
            if i > 0:
                sending_mail()
            i = 0

finally:
    picam2.close()
    print('꼼짝마, 감시카메라 시스템 종료!')        
    GPIO.cleanup()
    sys.exit()


