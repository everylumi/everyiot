﻿from picamera import PiCamera 
from time import sleep 

camera = PiCamera() 

camera.resolution = (1920, 1080)
camera.framerate = 15

camera.start_recording('/home/pi/Desktop/video.h264') 
sleep(5) 
camera.stop_recording()

print('영상 녹화 완료') 


