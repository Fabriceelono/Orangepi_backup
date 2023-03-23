import time

import wiringpi

import sys



#SETUP

print("Start")

pinLed = 2

pinSwitch = 1

wiringpi.wiringPiSetup()

wiringpi.pinMode(pinLed, 1)            # Set pin to mode 1 ( OUTPUT )

wiringpi.pinMode(pinSwitch, 0)         # Set pin to mode 0 ( INPUT )



#infinite loop - stop using CTRL-C

while True:

    # Capacitance measurement code

    wiringpi.pinMode(pinSwitch, 1)   # Set pin to mode 1 ( OUTPUT )

    wiringpi.digitalWrite(pinSwitch, 0)   # Set output to 0 ( LOW )

    time.sleep(0.1)   # Time to discharge the capacitor

    wiringpi.pinMode(pinSwitch, 0)   # Set pin to mode 0 ( INPUT )

    start_time = time.time()

    while wiringpi.digitalRead(pinSwitch) == 0:

        # Wait for input to go high

        pass

    stop_time = time.time()

    interval = stop_time - start_time

    print("Interval:", interval)