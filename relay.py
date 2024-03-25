

class Relay:
    def __init__(self):
        try:
        except ValueError:
            GPIO.setmode(GPIO.BCM)
        except RuntimeError:
            GPIO.setmode(GPIO.BOARD)

    def __del__(self):

    def open(self):

    def close(self):
