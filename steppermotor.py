import wiringpi
import time
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

# Set up the GPIO pins
wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN1, 1)
wiringpi.pinMode(PIN2, 1)
wiringpi.pinMode(PIN3, 1)
wiringpi.pinMode(PIN4, 1)
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
# Rotate the stepper motor
rotate(STEPS_PER_REVOLUTION, 'CW', 5) # Rotate one full revolution clockwise at 5 RPM
time.sleep(1) # Wait for 1 second
rotate(STEPS_PER_REVOLUTION, 'CCW', 10) # Rotate one full revolution counterclockwise at 10 RPM
time.sleep(1) # Wait for 1 second