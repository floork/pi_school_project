"""
This is the main file to read the data from the sensor and display it on the 7 segment led panel.
"""

import time

import adafruit_character_lcd.character_lcd_i2c as character_lcd
import board
import busio
import dht11
import RPi.GPIO as GPIO
from adafruit_ht16k33.segments import Seg7x4

# Definiere LCD Zeilen und Spaltenanzahl.
lcd_columns = 16
lcd_rows = 2

# Initialisierung I2C Bus
i2c = busio.I2C(board.SCL, board.SDA)

# Festlegen des LCDs in die Variable LCD

lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)

# 7 segment led panel
segment = Seg7x4(i2c, address=0x70)
segment.fill(0)


def init_gpio():
    """
    initialisierung der GPIO Pins
    """
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()


def get_data() -> dict:
    """
    Daten aus Sensor auslesen und als dictionary zurückgeben
    """
    instance = dht11.DHT11(pin=4)
    result = instance.read()
    while not result.is_valid():
        result = instance.read()

    return {"temp": result.temperature, "humidity": result.humidity}


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


def led_print(data: dict):
    """
    Daten auf LED Panel ausgeben
    """
    try:
        segment.fill(0)

        temp = str(data.get("temp", 0))
        temperature_list = list(temp)
        print(data)
        segment[0] = temperature_list[0]
        segment[1] = temperature_list[1]
        segment[1] = "."
        segment[2] = temperature_list[3]
        segment[3] = "C"

        time.sleep(10)

        segment.fill(0)
        humidity = str(data.get("humidity", 0))
        humidity_list = list(humidity)

        if data["humidity"] == 100:
            segment[0] = "1"
            segment[1] = "0"
            segment[2] = "0"
            time.sleep(10)
            return

        segment[0] = humidity_list[0]
        segment[1] = humidity_list[1]
        segment[1] = "."
        segment[2] = "0"
        segment[3] = "L"
        time.sleep(10)

    except KeyboardInterrupt:
        segment.fill(0)


def main():
    """
    Main Funktion des Programms
    """
    init_gpio()

    while True:
        data = get_data()

        led_print(data)
        lcd_print(f"temp: {data['temp']}", f"humidity: {data['humidity']}")


if __name__ == "__main__":
    main()
