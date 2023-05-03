import wiringpi
import time

# Define the number of steps per revolution of the stepper motor
STEPS_PER_REVOLUTION = 2038

# Define the GPIO pins for the stepper motor
# These are BCM pin numbers, which correspond to physical pin numbers on the Raspberry Pi
# For example, BCM pin 17 corresponds to physical pin 11 on the Pi's GPIO header
PIN1 = 17
PIN2 = 18
PIN3 = 27
PIN4 = 22

# Define the step sequence for the stepper motor
# This is the sequence of signals that need to be sent to the motor's coils to make it rotate one step
# The sequence is a 2D list where each row represents one step of the motor
# Each column of the row corresponds to a different coil of the motor
# The values in each column are either 1 or 0, indicating whether that coil should be energized or not
# The sequence should be designed so that the motor rotates smoothly and without skipping steps
SEQUENCE = [[1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]]

# Set up the GPIO pins
wiringpi.wiringPiSetupGpio()  # Use BCM pin numbers instead of WiringPi pin numbers
wiringpi.pinMode(PIN1, wiringpi.OUTPUT)
wiringpi.pinMode(PIN2, wiringpi.OUTPUT)
wiringpi.pinMode(PIN3, wiringpi.OUTPUT)
wiringpi.pinMode(PIN4, wiringpi.OUTPUT)

# Function to rotate the stepper motor a specified number of steps
def rotate(steps, direction, speed):
    # Calculate the delay time between steps based on the desired speed in RPM
    delay_time = 60.0 / (STEPS_PER_REVOLUTION * speed)
    
    # Determine the step sequence to use based on the desired direction of rotation
    if direction == 'CW':
        sequence = SEQUENCE
    else:
        sequence = SEQUENCE[::-1]  # Reverse the sequence for counterclockwise rotation
    
    # Iterate through the specified number of steps and activate the coils of the motor accordingly
    for i in range(steps):
        for step in sequence:
            wiringpi.digitalWrite(PIN1, step[0])
            wiringpi.digitalWrite(PIN2, step[1])
            wiringpi.digitalWrite(PIN3, step[2])
            wiringpi.digitalWrite(PIN4, step[3])
            time.sleep(delay_time)

# Rotate the stepper motor
rotate(STEPS_PER_REVOLUTION, 'CW', 5)  # Rotate one full revolution clockwise at 5 RPM
time.sleep(1)  # Wait for 1 second
rotate(STEPS_PER_REVOLUTION, 'CCW', 10)  # Rotate one full revolution counterclockwise at 10 RPM
time.sleep(1)  # Wait for 1 second
