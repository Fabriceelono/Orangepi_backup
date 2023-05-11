import time
import wiringpi


# Set up GPIO pin numbering mode
wiringpi.wiringPiSetup()


# Set up the GPIO pin connected to the relay as an output
relay_pin = 12# Replace with the actual pin number you're using
wiringpi.pinMode(relay_pin, 1)


# Turn the relay on and off 5 times with a 1-second delay between each change
for i in range(5):
    wiringpi.digitalWrite(relay_pin, wiringpi.HIGH)
    time.sleep(1)
    wiringpi.digitalWrite(relay_pin, wiringpi.LOW)
    time.sleep(1)


# Clean up GPIO settings
wiringpi.digitalWrite(relay_pin, wiringpi.LOW)
wiringpi.pinMode(relay_pin, wiringpi.INPUT)