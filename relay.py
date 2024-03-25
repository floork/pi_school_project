import RPi.GPIO as GPIO


class Relay:
    def __init__(self):
        self.relay_pin = 40
        try:
            GPIO.setmode(GPIO.BOARD)
        except ValueError:
            GPIO.setmode(GPIO.BCM)
        except RuntimeError:
            GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.relay_pin, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def open(self):
        GPIO.output(self.relay_pin, GPIO.LOW)

    def close(self):
        GPIO.output(self.relay_pin, GPIO.HIGH)
