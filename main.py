"""
This is the main file to read the data from the sensor and display it on the 7 segment led panel.
"""

import time

import adafruit_character_lcd.character_lcd_i2c as character_lcd
import board
import busio
import dht11
import RPi.GPIO as GPIO
import smbus
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

if GPIO.RPI_REVISION == 1:
    bus = smbus.SMBus(0)
else:
    bus = smbus.SMBus(1)


class LightSensor:
    def __init__(self):
        # Definiere Konstante vom Datenblatt

        self.DEVICE = 0x5C  # Standart I2C Geräteadresse

        self.POWER_DOWN = 0x00  # Kein aktiver zustand
        self.POWER_ON = 0x01  # Betriebsbereit
        self.RESET = 0x07  # Reset des Data registers

        # Starte Messungen ab 4 Lux.
        self.CONTINUOUS_LOW_RES_MODE = 0x13
        # Starte Messungen ab 1 Lux.
        self.CONTINUOUS_HIGH_RES_MODE_1 = 0x10
        # Starte Messungen ab 0.5 Lux.
        self.CONTINUOUS_HIGH_RES_MODE_2 = 0x11
        # Starte Messungen ab 1 Lux.
        # Nach messung wird Gerät in einen inaktiven Zustand gesetzt.
        self.ONE_TIME_HIGH_RES_MODE_1 = 0x20
        # Starte Messungen ab 0.5 Lux.
        # Nach messung wird Gerät in einen inaktiven Zustand gesetzt.
        self.ONE_TIME_HIGH_RES_MODE_2 = 0x21
        # Starte Messungen ab 4 Lux.
        # Nach messung wird Gerät in einen inaktiven Zustand gesetzt.
        self.ONE_TIME_LOW_RES_MODE = 0x23

    def convertToNumber(self, data):
        # Einfache Funktion um 2 Bytes Daten
        # in eine Dezimalzahl umzuwandeln
        return (data[1] + (256 * data[0])) / 1.2

    def readLight(self):
        data = bus.read_i2c_block_data(self.DEVICE, self.ONE_TIME_HIGH_RES_MODE_1)
        return self.convertToNumber(data)


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
    light_sensor = LightSensor()
    while not result.is_valid():
        result = instance.read()

    return {
        "temp": result.temperature,
        "humidity": result.humidity,
        "light": light_sensor.readLight(),
    }


def lcd_print(output: str, output2: str):
    # Hintergrundbeleuchtung einschalten

    lcd.backlight = True

    # Zwei Worte mit Zeilenumbruch werden ausgegeben
    lcd.message = output + "\n" + output2

    # Cursor anzeigen lassen.


def led_print(data: dict):
    """
    Daten auf LED Panel ausgeben
    """
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


def main():
    """
    Main Funktion des Programms
    """
    init_gpio()

    while True:
        try:
            data = get_data()

            lcd_print(f"temp: {data['temp']}", f"humidity: {data['humidity']}")
            led_print(data)
        except KeyboardInterrupt:
            # LCD ausschalten.

            lcd.clear()
            lcd.backlight = False

            segment.fill(0)

            # GPIO.cleanup()
            return


if __name__ == "__main__":
    main()
