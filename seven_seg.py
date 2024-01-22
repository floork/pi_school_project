import board
import busio
from adafruit_ht16k33.segments import Seg7x4


class SegementLed:
    def __init__(self):
        # Initialisierung I2C Bus --> 7seg
        i2c = busio.I2C(board.SCL, board.SDA)

        # 7 segment led panel
        self.segment = Seg7x4(i2c, address=0x70)
        self.segment.fill(0)

    def __del__(self):
        self.segment.fill(0)

    def print(self, data: float, data_type: str) -> None:
        """
        Daten auf LED Panel ausgeben
        """
        self.segment.fill(0)

        data_str = str(data)
        data_list = list(data_str)

        # for convenience we print the data to the terminal
        print(f"{data_type}: {data}")

        if data_type == "humidity":
            if data == 100:
                self.segment[0] = "1"
                self.segment[1] = "0"
                self.segment[2] = "0"
                return

            self.segment[0] = data_list[0]
            self.segment[1] = data_list[1]
            self.segment[1] = "."
            self.segment[2] = "0"
            self.segment[3] = "L"
            return

        # print the temperature
        self.segment[0] = data_list[0]
        self.segment[1] = data_list[1]
        self.segment[1] = "."
        self.segment[2] = data_list[3]
        self.segment[3] = "C"
