from picamera import PiCamera, Color
from time import sleep 

camera = PiCamera() 

camera.resolution = (2592, 1944)
camera.brightness = 70
camera.contrast = 50

camera.annotate_text = "Hello world!"
camera.annotate_text_size = 50
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')

camera.capture('/home/pi/Desktop/image.jpg')

camera.rotation = 90
camera.capture('/home/pi/Desktop/image_90.jpg')

print('사진 저장 완료') 


