import wiringpi
import time


def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)    # Write 1 ( HIGH ) to pin
    time.sleep(0.1)
    wiringpi.digitalWrite(_pin, 0)    # Write 1 ( HIGH ) to pin
    time.sleep(0.1)

# Define the GPIO pins connected to the ULN2003 inputs
IN1 = 3
IN2 = 11
IN3 = 13
IN4 = 15

# Set the GPIO pins as outputs
print("Start")
wiringpi.wiringPiSetup() 
wiringpi.pinMode(IN1, 1) 
wiringpi.pinMode(IN2, 1) 
wiringpi.pinMode(IN3, 1)
wiringpi.pinMode(IN4, 1)  

# Blink the LEDs
for i in range(0,10):
    blink(IN1)
    blink(IN2)
    blink(IN3)
    blink(IN4)
    time.sleep(1)

# Cleanup the GPIO pins
print('done')