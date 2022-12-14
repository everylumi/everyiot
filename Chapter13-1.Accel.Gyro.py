from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)

'''
민감도 범위, 주석을 해제하고 희망하는 측정범위를 입력
Accelerometer: ACCEL_RANGE_2G, ACCEL_RANGE_4G, ACCEL_RANGE_8G, ACCEL_RANGE_16G  
Gyroscope: GYRO_RANGE_250DEG, GYRO_RANGE_500DEG, GYRO_RANGE_1000DEG, GYRO_RANGE_2000DEG 
'''
#sensor.set_accel_range(sensor.ACCEL_RANGE_2G)   #미설정시 defalut: ACCEL_RANGE_2G
#sensor.set_gyro_range(sensor.GYRO_RANGE_250DEG) #미설정시 defalut: AGYRO_RANGE_250DEG

gyro_x = 0
gyro_y = 0
gyro_z = 0
sumGX = 0
sumGY = 0
sumGZ = 0
angle_x_prev = 0
angle_y_prev = 0
angle_z_prev = 0

t_prev = int(time.time()*1000000.0)
alpha = 0.96
beta = 5

gyro_data = sensor.get_gyro_data()
for i in range(0, 10, 1):
    sumGX = sumGX + gyro_data['x']
    sumGY = sumGY + gyro_data['y']
    sumGZ = sumGZ + gyro_data['z']
gyro_Base_x =  sumGX / 10      
gyro_Base_y =  sumGY / 10
gyro_Base_z =  sumGZ / 10    

while True:
    print("\nAccelerometer data")
    accel_data = sensor.get_accel_data()
    print(" x: " + str(accel_data['x']))
    print(" y: " + str(accel_data['y']))
    print(" z: " + str(accel_data['z']))

    accel_date_angle = sensor.get_accel_rotation()
    print(" - X_Rotation: ",round(accel_date_angle['y'],1), "\u00b0")
    print(" - Y_Rotation: ",round(accel_date_angle['x'],1), "\u00b0")
    print(" - Z_Rotation: ",round(accel_date_angle['z'],1), "\u00b0")
   
    print("Gyroscope data")
    gyro_data = sensor.get_gyro_data()
    print(" x: " + str(gyro_data['x']))
    print(" y: " + str(gyro_data['y']))
    print(" z: " + str(gyro_data['z']))
    
    print("Angle Data(Accelerometer + Gyroscope)")

    t_now = int(time.time()*1000000.0)
    dt_n = t_now - t_prev
    t_prev = t_now
    dt = dt_n / 1000000

    gyro_x = (sensor.get_gyro_data()['x'] - gyro_Base_x) * dt
    gyro_y = (sensor.get_gyro_data()['y'] - gyro_Base_y) * dt
    gyro_z = (sensor.get_gyro_data()['z'] - gyro_Base_z) * dt

    if abs(gyro_x) > beta:
        angle_x = alpha * (angle_x_prev + gyro_x) + (1-alpha) * accel_date_angle['y']
        angle_x_prev = angle_x
    else:
        angle_x = accel_date_angle['y']
        angle_x_prev = angle_x
    
    if abs(gyro_y) > beta:
        angle_y = alpha * (angle_y_prev + gyro_y) + (1-alpha) * accel_date_angle['x']
        angle_y_prev = angle_y
    else:
        angle_y = accel_date_angle['x']
        angle_y_prev = angle_y
    
    angle_z = angle_z_prev + gyro_z
    angle_z_prev = angle_z

    print(" - X_Rotation: ",round(angle_x,1),"\u00b0")
    print(" - Y_Rotation: ",round(angle_y,1), "\u00b0")
    print(" - Z_Rotation: ",round(angle_z,1), "\u00b0")

    temp = sensor.get_temp()
    print("Temperature: ",round(temp,1), "\u00b0C")
    
    time.sleep(0.5)

