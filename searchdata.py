import csv
filename="output.csv"

def searchname(filename,name):
    isFound = False
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Name"] == name:
                isFound = True
                break
    return isFound



name = input("Enter name to search: ")
if searchname(filename,name):
    print("Name found")
else:
    print("Name not found")