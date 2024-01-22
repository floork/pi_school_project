import pandas as pd


class CSV:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data: dict):
        df = pd.DataFrame(data, index=[0])
        df.to_csv(self.filename, mode="a", header=data.keys(), index=False)
