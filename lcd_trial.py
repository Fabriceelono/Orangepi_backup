import time
import wiringpi
import spidev
from class_lcd import LCD

def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)

PIN_OUT     =   {  
                'SCLK'  :   14,
                'DIN'   :   11,
                'DC'    :   8, 
                'CS'    :   13, 
                
                'RST'   :   10,
                'LED'   :   16, #backlight   
}

#IN THIS CODE WE USE W13 (PIN 22) AS CHIP SELECT
pin_CS_lcd = 13
wiringpi.wiringPiSetup() 
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)  #(channel, port, speed, mode)
wiringpi.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd_1 = LCD(PIN_OUT)

def get_time():
    # Get the current time in HH:MM:SS format
    t = time.localtime()
    return f"{t.tm_hour:02}:{t.tm_min:02}:{t.tm_sec:02}"

try:
    lcd_1.clear()
    lcd_1.set_backlight(1)
    while True:
        ActivateLCD()
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string("Current Time: ")
        lcd_1.put_string("\n"+str(get_time()))
        lcd_1.refresh()
        DeactivateLCD()
        time.sleep(1)
except KeyboardInterrupt:
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD()
    print("\nProgram terminated")
