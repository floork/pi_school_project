import RPi.GPIO as GPIO


class Relay:
    def __init__(self):
        self.relay_pin = 40
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay_pin, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def open(self):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.relay_pin, GPIO.OUT)
            GPIO.output(self.relay_pin, GPIO.LOW)
        except:
            pass
        GPIO.output(self.relay_pin, GPIO.LOW)

    def close(self):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.relay_pin, GPIO.OUT)
            GPIO.output(self.relay_pin, GPIO.HIGH)
        except:
            pass
        GPIO.output(self.relay_pin, GPIO.HIGH)
