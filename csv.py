import csv


class CSV:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "w")
        self.csv = csv
        self.writer = csv.writer(
            self.file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )

    def __del__(self):
        self.file.close()

    def write(self, data):
        self.writer.writerow(data)

    def dict_writer(self, obj: dict):
        self.csv.DictWriter(self.file, fieldnames=obj.keys())
