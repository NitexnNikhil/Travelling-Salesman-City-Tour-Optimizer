import csv

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        return [(row[0], float(row[1]), float(row[2])) for row in reader]
