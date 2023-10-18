import RPi.GPIO as GPIO
import dht11
import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Definiere LCD Zeilen und Spaltenanzahl.
lcd_columns = 16
lcd_rows = 2

# Initialisierung I2C Bus
i2c = busio.I2C(board.SCL, board.SDA)

# 7 segment led panel
segment = Seg7x4(i2c, address=0x70)
segment.fill(0)

# Festlegen des LCDs in die Variable LCD
# lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)


def lcd_print(output: str, output2: str):
    try:
        # Hintergrundbeleuchtung einschalten
        lcd.backlight = True

        # Zwei Worte mit Zeilenumbruch werden ausgegeben
        lcd.message = output + "\n" + output2

    except KeyboardInterrupt:
        # LCD ausschalten.
        lcd.clear()
        lcd.backlight = False


def main():
    # initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    # read data using pin 14
    instance = dht11.DHT11(pin=4)

    for _ in range(30):
        result = instance.read()

        while not result.is_valid():  # read until valid values
            result = instance.read()

        lcd_print(
            "Temp: %-3.1f C" % result.temperature, "Humidity: %-3.1f %%" % result.humidity
        )

        time.sleep(10)
        # Cursor anzeigen lassen.
        lcd.clear()

# if __name__ == __main__:
#     main()
main()
"""
try:
  while(True):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    segment.fill(0)

    # Anzeige für die Stunden.
    segment[0] =  str(int(hour / 10))     # Zehnerzahlen
    segment[1] =   str(hour % 10)         # Einerzahlen
    # Anzeige für die Minuten.
    segment[2] =   str(int(minute / 10))   # Zehnerzahlen
    segment[3] =   str(minute % 10)        # Einerzahlen
    #segment.colon = False

    if second % 2  == 0:
        segment.colon = True
    else:
        segment.colon = False

    segment.show() # Wird benötigt um die Display LEDs zu updaten.

    time.sleep(1) # Warte eine Sekunde
except KeyboardInterrupt:

    segment.fill(0) """
