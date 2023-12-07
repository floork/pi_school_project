"""
This is the main file to read the data from the sensor and display it on the 7 segment led panel.
"""
import time

from lcd import LcdScreen
from matrix import Matrix
from seven_seg import SegementLed
from temp_humid_sensor import DHT11


def main():
    """
    Main Funktion des Programms
    """
    while True:
        try:
            # Read data from sensor
            dht11 = DHT11()
            data = dht11.data()

            # Print data on the 7 segment led panel
            segment_led = SegementLed()
            segment_led.print(data["humidity"], "humidity")
            time.sleep(10)
            segment_led.print(data["temp"], "temp")
            time.sleep(10)

            # Print data on the matrix
            matrix = Matrix()
            matrix.print(data["light"])

            # Print data on the lcd screen
            lcd = LcdScreen()
            lcd.print(f"temp: {data['temp']}", f"humidity: {data['humidity']}")

        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    main()
