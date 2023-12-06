import adafruit_character_lcd.character_lcd_i2c as character_lcd
import busio
import board


class LcdScreen:
    def __init__(self):
        # Initialisierung I2C Bus --> LCD
        i2c = busio.I2C(board.SCL, board.SDA)
        # Definiere LCD Zeilen und Spaltenanzahl.
        lcd_columns = 16
        lcd_rows = 2

        # Festlegen des LCDs in die Variable LCD
        self.lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)

    def __del__(self):
        pass

    def print(self, output: str, output2: str) -> None:
        # Hintergrundbeleuchtung einschalten

        self.lcd.backlight = True

        # Zwei Worte mit Zeilenumbruch werden ausgegeben
        self.lcd.message = output + "\n" + output2
