with open("d://sample2.txt", "w") as fp:
    print("Enter the contents from keyboard type STOP to finishi typing\n")

    while True:
        line = input("Enter a line")
        if line.upper() == "STOP":
            break
        fp.write(line + "\n")
print("File contents written to disk")
