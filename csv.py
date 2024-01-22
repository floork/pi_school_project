import csv


class CSV:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data: dict):
        csvfile = open(self.filename, "a")
        c = csv.DictWriter(csvfile, fieldnames=data.keys())
        c.writeheader()

        c.writerow(data)

        csvfile.close()
