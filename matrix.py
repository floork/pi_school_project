import time

from luma.core import legacy
from luma.core.interface.serial import noop, spi
from luma.core.render import canvas
from luma.led_matrix.device import max7219


class Matrix:
    def __init__(self):
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

    def print(self, light) -> None:
        """
        Daten auf LED Panel ausgeben
        """
        flight = float(light)

        if flight <= 35_000:
            self.arrow_down()
            return

        if flight > 60_000:
            self.arrow_up()
            return

        self.ok()
