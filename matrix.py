from luma.core.interface.serial import noop, spi
from luma.core.legacy import show_message
from luma.core.legacy.font import CP437_FONT, proportional
from luma.led_matrix.device import max7219


class Matrix:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def print(self, light) -> None:
        """
        Daten auf LED Panel ausgeben
        """

        cascaded = 1
        block_orientation = 90
        rotate = 0
        # Matrix Gerät festlegen und erstellen.
        serial = spi(port=0, device=1, gpio=noop())
        device = max7219(
            serial,
            cascaded=cascaded or 1,
            block_orientation=block_orientation,
            rotate=rotate or 0,
        )
        # Matrix Initialisierung in der Konsole anzeigen
        # print("[-] Matrix initialized")

        # Joy-IT in der Matrix anzeigen
        flight = float(light)
        msg = ""
        if flight <= 1000:
            msg = "!Ok"
        else:
            msg = "OK"
        # Ausgegebenen Text in der Konsole Anzeigen
        show_message(
            device, msg, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1
        )
