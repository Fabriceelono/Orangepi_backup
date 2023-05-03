import wiringpi
import time

# Define the number of steps per revolution
STEPS_PER_REVOLUTION = 2038

# Define the GPIO pins for the stepper motor
PIN1 = 0  # BCM GPIO 17 Physical 11
PIN2 = 1  # BCM GPIO 18 ,12
PIN3 = 2  # BCM GPIO 27, 13
PIN4 = 3  # BCM GPIO 22,15

# Define the step sequence for the stepper motor
SEQUENCE = [[1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0]]

# Set up the GPIO pins
wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN1, wiringpi.OUTPUT)
wiringpi.pinMode(PIN2, wiringpi.OUTPUT)
wiringpi.pinMode(PIN3, wiringpi.OUTPUT)
wiringpi.pinMode(PIN4, wiringpi.OUTPUT)

# Function to rotate the stepper motor a specified number of steps
def rotate(steps, direction, speed):
    delay_time = 0.01
    #60.0 / (STEPS_PER_REVOLUTION * speed)
    for i in range(steps):
        for j in range(4):
            wiringpi.digitalWrite(PIN1, SEQUENCE[j][0])
            wiringpi.digitalWrite(PIN2, SEQUENCE[j][1])
            wiringpi.digitalWrite(PIN3, SEQUENCE[j][2])
            wiringpi.digitalWrite(PIN4, SEQUENCE[j][3])
            time.sleep(delay_time)
    if direction == 'CCW':
        SEQUENCE.reverse()

# Rotate the stepper motor
rotate(2038, 'CW', 5) # Rotate 1 revolution clockwise at 5 RPM
time.sleep(1) # Wait for 1 second
rotate(2038, 'CCW', 10) # Rotate 1 revolution counterclockwise at 10 RPM
time.sleep(1) # Wait for 1 second
