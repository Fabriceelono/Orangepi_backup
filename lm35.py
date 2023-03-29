import wiringpi
import time
import json
import requests


# Define ADC pins
pin_CS_adc = 16  # change to the appropriate pin

# Define LM35 pin
lm35_pin = 0     # change to the appropriate pin

# Initialize wiringpi
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin_CS_adc, wiringpi.GPIO.OUTPUT)
wiringpi.wiringPiSPISetup(1, 1000000)  # MCP3008 is on SPI channel 1, set speed to 1MHz
url="http://iotessentialsr0912443.hub.ubeac.io/iotessfabrice"
uid="iotessfabrice"

# Define LM35 temperature sensor function
def read_lm35():
    # Read ADC value from MCP3008
    wiringpi.digitalWrite(pin_CS_adc, wiringpi.GPIO.LOW)
    adc_command = bytes([1, (8 + lm35_pin) << 4, 0])
    revlen, recvData = wiringpi.wiringPiSPIDataRW(1, adc_command)
    wiringpi.digitalWrite(pin_CS_adc, wiringpi.GPIO.HIGH)
    
    # Convert ADC value to temperature in degrees Celsius
    adc_value = ((recvData[1] & 3) << 8) + recvData[2]
    temp_celsius = adc_value * 330 / 1023
    
    # Return temperature
    return temp_celsius

# Main loop
try:
    while True:
        temp_celsius = read_lm35()
        data= {
        "id": uid,
        "sensors":[{
            'id': 'adc ch0',
            'data': temp_celsius
             }]
        }
        r = requests.post(url, verify=False, json=data)

        print("Temperature: {:.1f} °C".format(temp_celsius))
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram terminated")