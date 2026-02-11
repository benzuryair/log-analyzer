import csv


def load_data(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        data = []
        for i in reader:
            data.append(i)

        return data
