from gpiozero import MotionSensor

pir = MotionSensor(21)

while True:
	pir.wait_for_motion()
	print("센서가 감지되었습니다.")
	pir.wait_for_no_motion()
    print('센서가 해제되었습니다.')

