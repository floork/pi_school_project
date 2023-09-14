import RPi.GPIO as GPIO

import dht11

import time

import board

import busio

import adafruit_character_lcd.character_lcd_i2c as character_lcd



# Definiere LCD Zeilen und Spaltenanzahl.

lcd_columns = 16

lcd_rows = 2



# Initialisierung I2C Bus

i2c = busio.I2C(board.SCL, board.SDA)



# Festlegen des LCDs in die Variable LCD

lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)





def lcd_print(output: str, output2: str):

    try:

        # Hintergrundbeleuchtung einschalten

        lcd.backlight = True



        # Zwei Worte mit Zeilenumbruch werden ausgegeben

        lcd.message = output + "\n" + output2



        time.sleep(10)

        # Cursor anzeigen lassen.

        lcd.clear()



    except KeyboardInterrupt:

        # LCD ausschalten.

        lcd.clear()

        lcd.backlight = False





def main():

    # initialize GPIO

    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)

    GPIO.cleanup()



    # read data using pin 14

    instance = dht11.DHT11(pin=4)

    result = instance.read()



    while not result.is_valid():  # read until valid values

        result = instance.read()



    for i in range(9):

        lcd_print(

            "Temp: %-3.1f C" % result.temperature, "Humidity: %-3.1f %%" % result.humidity

        )



#if __name__ == __main__:
#
#    main()
main()

