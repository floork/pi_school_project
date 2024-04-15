import RPi.GPIO as GPIO


class Relay:
    def __init__(self):
        self.relay_pin = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay_pin, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def open(self):
        GPIO.output(self.relay_pin, GPIO.LOW)

    def close(self):
        GPIO.output(self.relay_pin, GPIO.HIGH)
