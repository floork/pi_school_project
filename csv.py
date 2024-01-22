import csv


class CSV:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "w")
        self.csv = csv

    def __del__(self):
        self.file.close()

    def write(self, data: dict):
        self.csv.DictWriter(self.file, fieldnames=data.keys())
