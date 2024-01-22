import csv


class CSV:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "w")

    def __del__(self):
        self.file.close()

    def write(self,  data: dict):
        file = self.file
        with open(file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys()

            writer.writeheader()
            for header in data.keys():
                writer.writerow(data[header])
