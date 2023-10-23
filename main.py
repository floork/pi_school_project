"""
This is the main file to read the data from the sensor and display it on the 7 segment led panel.
"""

import time

import adafruit_character_lcd.character_lcd_i2c as character_lcd
import board
import busio
import dht11
import RPi.GPIO as GPIO

# Definiere LCD Zeilen und Spaltenanzahl.
lcd_columns = 16
lcd_rows = 2

# Initialisierung I2C Bus
i2c = busio.I2C(board.SCL, board.SDA)

# 7 segment led panel
segment = Seg7x4(i2c, address=0x70)
segment.fill(0)


def led_print(output: list, data_type: str):
    """
    print the temperature and humidity
    """
    try:
        if data_type == "temp":
            segment[0] = str(output[0])
            segment[1] = str(output[1])
            segment.colon = True
            segment[2] = str(output[3])
            segment[3] = "C"

        elif data_type == "humidity":
            segment[0] = str(output[0])
            segment[1] = str(output[1])
            segment[2] = str(output[3])
            segment[3] = "%"

        segment.show()

    except KeyboardInterrupt:
        segment.fill(0)


def main():
    """
    main function to read the data from the sensor
    """
    # initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    # read data using pin 14
    instance = dht11.DHT11(pin=4)

    for _ in range(30):
        result = instance.read()

        while not result.is_valid():  # read until valid values
            result = instance.read()

        temp = result.temperature.split()
        humidity = result.humidity.split()

        led_print(temp, "temp")
        time.sleep(5)

        led_print(humidity, "humidity")
        time.sleep(5)


if __name__ == "__main__":
    main()
