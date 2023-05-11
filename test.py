import time
import wiringpi
import sys

# Define the number of steps per revolution of the stepper motor
STEPS_PER_REVOLUTION = 2038
PIN1 = 3
PIN2 = 4
PIN3 = 6
PIN4 = 9
SEQUENCE = [[1, 0, 0, 1],
[1, 0, 0, 0],
[1, 1, 0, 0],
[0, 1, 0, 0],
[0, 1, 1, 0],
[0, 0, 1, 0],
[0, 0, 1, 1],
[0, 0, 0, 1]]
#SETUP
wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN1, 1)
wiringpi.pinMode(PIN2, 1)
wiringpi.pinMode(PIN3, 1)
wiringpi.pinMode(PIN4, 1)
print("Start")
pinLed = 2
pinSwitch = 11
#connected to wiriingpin 11
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pinLed, 1)            # Set pin to mode 1 ( OUTPUT )
wiringpi.pinMode(pinSwitch, 0)         # Set pin to mode 0 ( INPUT )

# Function to rotate the stepper motor a specified number of steps
def rotate(steps, direction, speed):

     # Calculate the delay time between steps based on the desired speed in RPM
    delay_time = 60.0 / (STEPS_PER_REVOLUTION * speed)
    # Determine the step sequence to use based on the desired direction of rotation
    if direction == 'CW':
        sequence = SEQUENCE

    else:

        sequence = SEQUENCE[::-1] # Reverse the sequence for counterclockwise rotation

    # Iterate through the specified number of steps and activate the coils of the motor accordingly

    for i in range(steps):

        for step in sequence:

            wiringpi.digitalWrite(PIN1, step[0])

            wiringpi.digitalWrite(PIN2, step[1])

            wiringpi.digitalWrite(PIN3, step[2])

            wiringpi.digitalWrite(PIN4, step[3])

            time.sleep(delay_time)
#infinite loop - stop using CTRL-C
while True:
    if(wiringpi.digitalRead(pinSwitch) == 0): #input is active low
        print("Button Pressed")
        time.sleep(0.3) #anti bouncing
        wiringpi.digitalWrite(pinLed, 1)    # Write 1 ( HIGH ) to LED
        rotate(STEPS_PER_REVOLUTION, 'CCW', 10) # Rotate one full revolution counterclockwise at 10 RPM
        time.sleep(0.01) # Wait for 1 second
    else:
        print("Button released")
        time.sleep(0.3) #anti bouncing
        wiringpi.digitalWrite(pinLed, 0)    # Write 0 ( LOW ) to led