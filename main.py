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

    # Read data from sensor
    dht11 = DHT11()

    while True:
        try:
            data = dht11.data()
            humudity = data["humidity"]
            temp = data["temp"]
            light = data["light"]

            # Print data on the matrix
            matrix = Matrix()
            matrix.print(light)

            # Print data on the lcd screen
            lcd = LcdScreen()
            lcd.print(f"temp: {temp}", f"humidity: {humudity}")

            # Print data on the 7 segment led panel
            segment_led = SegementLed()
            segment_led.print(humudity, "humidity")
            time.sleep(10)
            segment_led.print(temp, "temp")
            time.sleep(10)

        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    main()
