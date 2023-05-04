import time
import wiringpi 
import sys

def blink(out_pin):
    for pin in out_pin:
        wiringpi.digitalWrite(pin,1)
        time.sleep(0.01)
        wiringpi.digitalWrite(pin,0)
        time.sleep(0.01)
 
print("Start task ") 
pins=[14,15,18,23]
wiringpi.wiringPiSetup()
for pin in pins:
    wiringpi.pinMode(pin, 1)            # Set pins to mode 1 ( OUTPUT )
while True:
    blink(pins)