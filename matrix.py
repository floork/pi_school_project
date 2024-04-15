import datetime

from luma.core import legacy
from luma.core.interface.serial import noop, spi
from luma.core.render import canvas
from luma.led_matrix.device import max7219

from relay import Relay


class Matrix:
    def __init__(self):
        self.relay = Relay()
        pass

    def __del__(self):
        pass

    def arrow_up(self) -> None:
        data = [[0x00, 0x04, 0x06, 0xFF, 0xFF, 0x06, 0x04, 0x00]]
        serial = spi(port=0, device=1, gpio=noop())
        device = max7219(serial, rotate=3)

        with canvas(device) as draw:
            # Note that "\0" is the zero-th character in the font (i.e the only one)
            legacy.text(draw, (0, 0), "\0", fill="white", font=data)

    def arrow_down(self) -> None:
        data = [[0x00, 0x04, 0x06, 0xFF, 0xFF, 0x06, 0x04, 0x00]]
        serial = spi(port=0, device=1, gpio=noop())
        device = max7219(serial, rotate=1)

        with canvas(device) as draw:
            # Note that "\0" is the zero-th character in the font (i.e the only one)
            legacy.text(draw, (0, 0), "\0", fill="white", font=data)

    def ok(self) -> None:
        data = [[0x30, 0x60, 0xC0, 0x60, 0x30, 0x18, 0x0C, 0x06]]
        serial = spi(port=0, device=1, gpio=noop())
        device = max7219(serial, rotate=3)

        with canvas(device) as draw:
            # Note that "\0" is the zero-th character in the font (i.e the only one)
            legacy.text(draw, (0, 0), "\0", fill="white", font=data)

    def is_night_time(self) -> bool:
        """
        Checks if it's currently night time.
        """
        current_hour = datetime.datetime.now().hour
        return (
            0 <= current_hour < 6
        )  # Assuming night time is between 12:00 AM and 6:00 AM

    def print(self, light) -> None:
        """
        Daten auf LED Panel ausgeben
        """
        flight = float(light)

        if self.is_night_time():
            # It's night time so the arrows should be down
            self.arrow_down()
            self.relay.close()  # Turn off the lights
            return

        # if flight <= 35_000:
        if flight <= 1000:
            self.arrow_down()
            self.relay.open()  # Turn on the lights
            return

        if flight > 1000:
            self.arrow_up()
            self.relay.close()  # Turn off the lights
            return

        self.ok()
