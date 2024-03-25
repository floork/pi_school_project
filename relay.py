import RPi.GPIO as GPIO


class Relay:
    def __init__(self):
        relay_pin = 40
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(relay_pin, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def open(self):
        GPIO.output(40, GPIO.LOW)

    def close(self):
        GPIO.output(40, GPIO.HIGH)
