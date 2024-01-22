"""
This is the main file to read the data from the sensor and display it on the 7 segment led panel.
"""
import datetime
import time
from csv import CSV

# from database import Database
from lcd import LcdScreen
from matrix import Matrix
from seven_seg import SegementLed
from temp_humid_sensor import DHT11


def main():
    """
    Main Funktion des Programms
    """
    # db = Database("data.sqlite")
    # db.create_table("My Data", ["time", "temp", "humidity", "light"])

    csv = CSV("data.csv")

    # Read data from sensor
    dht11 = DHT11()

    while True:
        try:
            data = dht11.data()

            humudity = data["humidity"]
            temp = data["temp"]
            light = data["light"]
            # current_time = datetime.datetime.now()
            full_dict = {
                "time": datetime.datetime.now(),
                "temp": temp,
                "humidity": humudity,
                "light": light,
            }

            csv.dict_writer(full_dict)

            # Save data in database
            # db.insert_data(
            #     "My Data",
            #     {
            #         "time": current_time,
            #         "temp": temp,
            #         "humidity": humudity,
            #         "light": light,
            #     },
            # )

            # Print data on the 7 segment led panel
            segment_led = SegementLed()
            segment_led.print(humudity, "humidity")
            time.sleep(10)
            segment_led.print(temp, "temp")
            time.sleep(10)

            # Print data on the matrix
            matrix = Matrix()
            matrix.print(light)

            # Print data on the lcd screen
            lcd = LcdScreen()
            lcd.print(f"temp: {temp}", f"humidity: {humudity}")

        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    main()
