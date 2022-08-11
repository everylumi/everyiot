from pms7003 import Pms7003Sensor, PmsSensorException

sensor = Pms7003Sensor('/dev/ttyUSB0')  #USB to TTL Serial 케이블 사용시
#sensor = Pms7003Sensor('/dev/ttyAMA0') #블루투스 중지후 라즈베리파이3 GPIO 연결시
#sensor = Pms7003Sensor('/dev/ttyAMA1') #UART 추가후 라즈베리파이4 GPIO 연결시

try:
    while True:
    
        Dust = sensor.read()
            
        print('\nStandard Condition ----------------------------')
        print('PM1.0:\t',Dust['pm1_0cf1'])
        print('PM2.5:\t',Dust['pm2_5cf1'])
        print('PM10:\t',Dust['pm10cf1'])
            
        print('\nCurrent Condition -----------------------------')
        print('PM1.0:\t',Dust['pm1_0'])
        print('PM2.5:\t',Dust['pm2_5'])
        print('PM10:\t',Dust['pm10'])
            
        print('\nNumber of particles in 0.1L of air-------------')
        print('>0.3μm:\t',Dust['n0_3'])
        print('>0.5μm:\t',Dust['n0_5'])
        print('>1.0μm:\t',Dust['n1_0'])
        print('>2.5μm:\t',Dust['n2_5'])
        print('>5.0μm:\t',Dust['n5_0'])
        print('>10μm:\t',Dust['n10'])   
        
except PmsSensorException:
    print('Connection problem')

finally:
    sensor.close()