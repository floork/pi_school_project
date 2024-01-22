import csv


class CSV:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "w")

    def __del__(self):
        self.file.close()

    def write(self, data: dict):
        csv.DictWriter(self.file, fieldnames=data.keys())
