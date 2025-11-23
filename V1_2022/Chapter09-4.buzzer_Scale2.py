from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
import time

bz = TonalBuzzer(12)

PWM_FREQ = [ 261.6256, \
             293.6648, \
             329.6276, \
             349.2282, \
             391.9954, \
             440.0000, \
             493.8833, \
             523.2511 ]

PWM_FREQ1 = ['C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4']

for i in range(0,8):
    bz.play(Tone(PWM_FREQ[i]))
    time.sleep(1.0)
    bz.stop()
    time.sleep(0.2)
    
for i in range(0,8):
    bz.play(Tone(PWM_FREQ1[i]))
    time.sleep(1.0)
    bz.stop()
    time.sleep(0.2)
