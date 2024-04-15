import RPi.GPIO as GPIO


class Relay:
    def __init__(self):
        self.relay_pin = 21
        self.state = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay_pin, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def open(self):
        if self.state is not None and self.state == "LOW":
            print("test")
            return

        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.relay_pin, GPIO.OUT)
            GPIO.output(self.relay_pin, GPIO.LOW)
            self.state = "LOW"
            print(self.state)
        except:
            pass

    def close(self):
        if self.state is not None and self.state == "HIGH":
            print("test")
            return
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.relay_pin, GPIO.OUT)
            GPIO.output(self.relay_pin, GPIO.HIGH)
            self.state = "HIGH"
            print(self.state)
        except:
            pass
