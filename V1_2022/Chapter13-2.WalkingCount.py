from mpu6050 import mpu6050
import time
import tm1637

CLK_PIN = 5
DIO_PIN = 4

sensor = mpu6050(0x68)   #Slave 모드일때는 0x69 
tm = tm1637.TM1637(clk=CLK_PIN, dio=DIO_PIN)

accel_date_angle_z_pre = 0
walking_No = 0
step_count = False
tm.number(walking_No)

while True:      

    print("\n가속도값 변화")
    accel_date_angle = sensor.get_accel_rotation()
    print("dz: ", abs(accel_date_angle['z']- accel_date_angle_z_pre))

    if abs(accel_date_angle['z']- accel_date_angle_z_pre) > 5 and step_count :
        step_count = False
        walking_No = walking_No + 1
        print('걸음수: ', walking_No)
        tm.number(walking_No)
    else:
        step_count = True

    accel_date_angle_z_pre = accel_date_angle['z']
    time.sleep(0.5)
