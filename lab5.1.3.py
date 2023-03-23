import wiringpi
import time

# Define the LED pins
LED_PIN_1 = 3  
LED_PIN_2 = 11 
LED_PIN_3 = 13   
LED_PIN_4 = 15   

# Initialize the WiringOP library
wiringpi.wiringPiSetup()

# Set up the LED pins as output
wiringpi.pinMode(LED_PIN_1, 1)
wiringpi.pinMode(LED_PIN_2, 1)
wiringpi.pinMode(LED_PIN_3, 1)
wiringpi.pinMode(LED_PIN_4, 1)

# Turn on the LEDs in sequence
while True:
    wiringpi.digitalWrite(LED_PIN_1, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(LED_PIN_1, 0)
    wiringpi.digitalWrite(LED_PIN_2, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(LED_PIN_2, 0)
    wiringpi.digitalWrite(LED_PIN_3, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(LED_PIN_3, 0)
    wiringpi.digitalWrite(LED_PIN_4, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(LED_PIN_4, 0)