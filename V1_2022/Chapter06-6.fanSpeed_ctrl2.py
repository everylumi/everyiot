from gpiozero import PWMLED
import time
import sys

FAN_PIN = 14
WAIT_TIME = 1
FAN_MIN = 30
PWM_FREQ = 25

tempSteps = [50, 70]
speedSteps = [0, 100]

hyst = 1

fan = PWMLED(FAN_PIN, active_high=True, initial_value=0, frequency=PWM_FREQ)

i = 0
cpuTemp = 0
fanSpeed = 0
cpuTempOld = 0
fanSpeedOld = 0

if len(speedSteps) != len(tempSteps):
    print("tempSteps 및 speedSteps 범위를 확인하세요.")
    exit(0)

try:
    while 1:
        cpuTempFile = open("/sys/class/thermal/thermal_zone0/temp", "r")
        cpuTemp = float(cpuTempFile.read()) / 1000
        cpuTempFile.close()

        if abs(cpuTemp - cpuTempOld) > hyst:

            if cpuTemp < tempSteps[0]:
                fanSpeed = speedSteps[0]

            elif cpuTemp >= tempSteps[len(tempSteps) - 1]:
                fanSpeed = speedSteps[len(tempSteps) - 1]

            else:
                for i in range(0, len(tempSteps) - 1):
                    if (cpuTemp >= tempSteps[i]) and (cpuTemp < tempSteps[i + 1]):
                        fanSpeed = round((speedSteps[i + 1] - speedSteps[i])
                                         / (tempSteps[i + 1] - tempSteps[i])
                                         * (cpuTemp - tempSteps[i])
                                         + speedSteps[i], 1)

            if fanSpeed != fanSpeedOld:
                if (fanSpeed != fanSpeedOld
                        and (fanSpeed >= FAN_MIN or fanSpeed == 0)):
                    fan.value = fanSpeed / 100
                    fanSpeedOld = fanSpeed
            cpuTempOld = cpuTemp

        time.sleep(WAIT_TIME)

except KeyboardInterrupt:
    print("Fan ctrl interrupted by keyboard")
    sys.exit()
