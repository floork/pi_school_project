"""
This is the main file to read the data from the sensor and display it on the 7 segment led panel.
"""
from temp_humid_sensor import DHT11
from matrix import Matrix
from seven_seg import SegementLed
from lcd import LcdScreen
import time


def main():
    """
    Main Funktion des Programms
    """
    while True:
        try:
            data = DHT11().data()

            SegementLed().print(data["humidity"], "humidity")
            time.sleep(10)
            SegementLed().print(data["temp"], "temp")
            time.sleep(10)
            Matrix().print(data["light"])
            LcdScreen().print(f"temp: {data['temp']}", f"humidity: {data['humidity']}")

        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    main()
