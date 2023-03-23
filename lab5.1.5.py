import wiringpi
import time

# Define the LED pins
LED_PIN_1 = 3# GPIO 0 (physical pin 11)
LED_PIN_2 = 11  # GPIO 1 (physical pin 12)
LED_PIN_3 = 13 # GPIO 2 (physical pin 13)
LED_PIN_4 = 15 # GPIO 3 (physical pin 15)

# Initialize the WiringOP library
wiringpi.wiringPiSetup()

# Set up the LED pins as output
wiringpi.pinMode(LED_PIN_1, 1)
wiringpi.pinMode(LED_PIN_2, 1)
wiringpi.pinMode(LED_PIN_3, 1)
wiringpi.pinMode(LED_PIN_4, 1)

while True:
    # Turn on LED1 and LED3
    wiringpi.digitalWrite(LED_PIN_1, 1)
    wiringpi.digitalWrite(LED_PIN_3, 1)
    
    # Wait for 1 second
    time.sleep(1)
    
    # Turn off LED1 and LED3
    wiringpi.digitalWrite(LED_PIN_1, 0)
    wiringpi.digitalWrite(LED_PIN_3, 0)
    
    # Turn on LED2 and LED4
    wiringpi.digitalWrite(LED_PIN_2, 1)
    wiringpi.digitalWrite(LED_PIN_4, 1)
    
    # Wait for 1 second
    time.sleep(1)
    
    # Turn off LED2 and LED4
    wiringpi.digitalWrite(LED_PIN_2, 0)
    wiringpi.digitalWrite(LED_PIN_4, 0)