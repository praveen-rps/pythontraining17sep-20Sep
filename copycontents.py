source_file = input("Enter the file path: ")
destination_file = input("Enter the destination file path: ")

with open(source_file, "r") as source, open(destination_file, "w") as destination:
   for line in source.readlines():
      destination.write(line)

print("File contents copied to another file...!")