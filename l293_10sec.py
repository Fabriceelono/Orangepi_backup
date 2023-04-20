import time
import wiringpi

def controlMotor(in1, in2, direction, wait):
    if direction == "forward":

        wiringpi.softPwmWrite(in1, 100)

        wiringpi.softPwmWrite(in2, 0)

    elif direction == "backward":

        wiringpi.softPwmWrite(in1, 0)

        wiringpi.softPwmWrite(in2, 100)

    elif direction == "stop":

        wiringpi.softPwmWrite(in1, 0)

        wiringpi.softPwmWrite(in2, 0)

    time.sleep(wait)



#SETUP

print("Start")

in1 = 2

in2 = 5

pause_time = 0.02

wiringpi.wiringPiSetup()



# Set pins as a softPWM output

wiringpi.softPwmCreate(in1, 0, 100)

wiringpi.softPwmCreate(in2, 0, 100)



# Start PWM

wiringpi.softPwmWrite(in1, 0)

wiringpi.softPwmWrite(in2, 0)



try:

    while True:

        controlMotor(in1, in2, "forward", 10)   # Run motor forward for 10 seconds

        controlMotor(in1, in2, "stop", 2)       # Stop motor for 2 seconds

        controlMotor(in1, in2, "backward", 10)  # Run motor backward for 10 seconds

        controlMotor(in1, in2, "stop", 2)       # Stop motor for 2 seconds



except KeyboardInterrupt:

    controlMotor(in1, in2, "stop", 0)          # Stop the motor

    print("\nDone")