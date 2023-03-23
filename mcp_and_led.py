import wiringpi
import time
import json
import requests

def ActivateADC ():

  wiringpi.digitalWrite(pin_CS_adc, 0) # Actived ADC using CS

  time.sleep(0.000005)

def DeactivateADC():

  wiringpi.digitalWrite(pin_CS_adc, 1) # Deactived ADC using CS

  time.sleep(0.000005)

def readadc(adcnum):

  if ((adcnum > 7) or (adcnum < 0)):

    return -1

  revlen, recvData = wiringpi.wiringPiSPIDataRW(1, bytes([1,(8+adcnum)<<4,0]))

  time.sleep(0.000005)

  adcout = ((recvData[1]&3) << 8) + recvData[2]

  return adcout



#Setup

pin_CS_adc = 16  #We will use w16 as CE, not the default pin w15!

wiringpi.wiringPiSetup()

wiringpi.pinMode(pin_CS_adc, 1) # Set ce to mode 1 ( OUTPUT )

wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0) #(channel, port, speed, mode)

LED_A_pin = 0 # set the pin for LED A

LED_B_pin = 1 # set the pin for LED B

wiringpi.pinMode(LED_A_pin, 1) # set LED A pin to OUTPUT mode

wiringpi.pinMode(LED_B_pin, 1) # set LED B pin to OUTPUT mode
url="http://iotessentialsr0912443.hub.ubeac.io/iotessfabrice"
uid="iotessfabrice"

#Main

try:

    while True:

        ActivateADC()

        tmp0 = readadc(0) # read channel 0

        DeactivateADC()



        ActivateADC()

        tmp1 = readadc(1) # read channel 1

        DeactivateADC()

        data= {
        "id":uid ,
        "sensors":[{
            'id': 'adc ch0',
            'data': tmp0
             },
             {'id': 'adc ch1',
             'data': tmp1
            }]
        }
     
        r = requests.post(url, verify=False, json=data)
        print(tmp0, tmp1)




        # compare voltages from potentiometers

        if tmp0 > tmp1:

            wiringpi.digitalWrite(LED_A_pin, 1) # turn on LED A

            wiringpi.digitalWrite(LED_B_pin, 0) # turn off LED B

        else:

            wiringpi.digitalWrite(LED_A_pin, 0) # turn off LED A

            wiringpi.digitalWrite(LED_B_pin, 1) # turn on LED B



        time.sleep(0.2)



except KeyboardInterrupt:

    DeactivateADC()

    wiringpi.digitalWrite(LED_A_pin, 0) # turn off LED A

    wiringpi.digitalWrite(LED_B_pin, 0) # turn off LED B

    print("\nProgram terminated")