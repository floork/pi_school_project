"""
This is the main file to read the data from the sensor and display it on the 7 segment led panel.
"""

import csv
import datetime
import time
from datetime import timezone

from database import Database
from lcd import LcdScreen
from matrix import Matrix
from seven_seg import SegementLed
from temp_humid_sensor import DHT11


def csv_writer(data, path):
    csv_file = open(path, "a", newline="")
    writer = csv.DictWriter(csv_file, fieldnames=data.keys())
    writer.writerow(data)
    csv_file.close()


def main():
    """
    Main Funktion des Programms
    """

    db = Database("database.db")
    db.create_table("My Data", ["time", "temp", "humidity", "light"])

    # Read data from sensor
    dht11 = DHT11()
    matrix = Matrix()

    while True:
        try:
            data = dht11.data()
            humudity = data["humidity"]
            temp = data["temp"]
            light = data["light"]

            dt = datetime.datetime.now(timezone.utc)
            utc_time = dt.replace(tzinfo=timezone.utc)
            utc_timestamp = utc_time.timestamp()

            full_dict = {
                "time": utc_timestamp,
                "temp": temp,
                "humidity": humudity,
                "light": light,
            }

            print(f"[DEBUG]: time -> {utc_timestamp}")
            print(f"[DEBUG]: temp -> {temp}")
            print(f"[DEBUG]: humudity -> {humudity}")
            print(f"[DEBUG]: light -> {light}")
            lenght = len(str(utc_timestamp)) + 20
            for _ in range(lenght):
                print("=", end="")
            print()

            csv_writer(full_dict, "data.csv")

            # Save data in database
            db.insert_data(
                "My Data",
                full_dict,
            )
            # Print data on the matrix
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
