import RPi.GPIO as GPIO
import dht11
from light_sensor import LightSensor


class DHT11:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

    def __del__(self):
        pass

    def data(self) -> dict:
        """
        Daten aus Sensor auslesen und als dictionary zurückgeben
        """
        instance = dht11.DHT11(pin=4)
        result = instance.read()
        light_sensor = LightSensor()
        while not result.is_valid():
            result = instance.read()

        return {
            "temp": result.temperature,
            "humidity": result.humidity,
            "light": round(light_sensor.readLight(), 2),
        }
