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
# Set the pin numbers
trigger_pin = 1
echo_pin = 2
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



# Initialize the wiringpi library
wiringpi.wiringPiSetup()



# Set the trigger pin as output and echo pin as input
wiringpi.pinMode(trigger_pin, wiringpi.OUTPUT)
wiringpi.pinMode(echo_pin, wiringpi.INPUT)



while True:
 # Send a trigger signal
 wiringpi.digitalWrite(trigger_pin, wiringpi.HIGH)
 time.sleep(0.00001)
 wiringpi.digitalWrite(trigger_pin, wiringpi.LOW)

 # Wait for the response signal
 while wiringpi.digitalRead(echo_pin) == wiringpi.LOW:
  signal_high = time.time()

 while wiringpi.digitalRead(echo_pin) == wiringpi.HIGH:
  signal_low = time.time()

 # Calculate distance
 time_passed = signal_low - signal_high
 distance = time_passed * 17000
 if distance<10:
    rotate(STEPS_PER_REVOLUTION, 'CW', 5) # Rotate one full revolution clockwise at 5 RPM
    time.sleep(0.01) # Wait for 1 second
 # Print distance and wait for 0.5 seconds
 print("Distance:", distance, "cm")
 time.sleep(0.5)