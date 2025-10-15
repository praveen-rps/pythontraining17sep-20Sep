import csv

filename = "data.csv"

with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        print(row)