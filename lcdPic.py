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
                'DC'    :   9, 
                'CS'    :   15, #We will not connect this pin! --> we use w13
                'RST'   :   10,
                'LED'   :   6, #backlight   
}

#IN THIS CODE WE USE W13 (PIN 22) AS CHIP SELECT
pin_CS_lcd = 13
wiringpi.wiringPiSetup() 
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)  #(channel, port, speed, mode)
wiringpi.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd_1 = LCD(PIN_OUT)

#image = Image.open('/home/orangepi/Orangepi_backup/epd_bitmap_.bin')

try:
    lcd_1.clear()
    lcd_1.set_backlight(1)
    while True:
        ActivateLCD()
        LCD.draw_image(lcd_1, '/home/orangepi/Orangepi_backup/epd_bitmap_.bin', 84, 48, x = 0, y = 0)
        lcd_1.refresh()
        DeactivateLCD()
        time.sleep(1)
        lcd_1.clear()
except KeyboardInterrupt:
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD()
    print("\nProgram terminated")


