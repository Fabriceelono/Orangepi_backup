import wiringpi
import time



# Set the pin numbers
trigger_pin = 1
echo_pin = 2



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

 # Print distance and wait for 0.5 seconds
 print("Distance:", distance, "cm")
 time.sleep(0.5)