"""
This is the main file to read the data from the sensor and display it on the 7 segment led panel.
"""

import time

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

# 7 segment led panel
segment = Seg7x4(i2c, address=0x70)
segment.fill(0)


def init_gpio():
    """
    initialize GPIO
    """
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()


def get_data() -> dict:
    """
    read the data from the sensor
    """
    instance = dht11.DHT11(pin=4)
    result = instance.read()
    while not result.is_valid():
        result = instance.read()

    return {"temp": result.temperature, "humidity": result.humidity}


def led_print(data: dict):
    try:
        temp = str(data.get("temp", 0))
        temperature_list = list(temp)
        print(data)
        for i in range(len(temperature_list)):
            output = temperature_list[i]
            if output == ".":
                pass
            if i == 1:
                segment[i] = output + "."
            else:
                segment[i] = output

        segment[3] = "C"

        time.sleep(10)

        humidity = str(data.get("humidity", 0))
        humidity_list = list(humidity)

        for i in range(len(humidity_list)):
            output = humidity_list[i]
            segment[i] = output

        time.sleep(10)

    except KeyboardInterrupt:
        segment.fill()


def main():
    """
    main function to read the data from the sensor
    """
    init_gpio()

    for _ in range(30):
        data = get_data()

        led_print(data)


if __name__ == "__main__":
    main()
