import csv
filename = "output.csv"

data = [
    ["Name", "Dept", "Designation"],
    ["Praveen", "Quality","Manager"],
    ["Sunil", "Quality", "Sr Technician"],
    ["Mohan", "Quality", "Lead"],
    ["Anil", "Finance", "Executive"]
  ]

with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("CSV data written successfully")