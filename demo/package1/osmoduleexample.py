from os import *



# getcwd()

print("The current working Dir", getcwd())
print("list of files in current working dir ", listdir("."))
print("The lisf of files and folder in c://demo", listdir("c://demo"))
print("One directory is creating in  C drive!")
#mkdir("../package2/testdir")
print("Directory is created...!")

"""
rmdir() --> used to remove the director in the current location
rmdir("/path/to/direcotry") -- remove the direcotory from the given path


"""

fd = open("c:/data/testpy.py", O_CREAT)
close(fd)

print("The file is created in the current location")

print(path.exists("c:/data/test1py.py"))
print("Is it a file ", path.isfile("c:/data/testpy.py"))
print("Is it a Directory ", path.isdir("c:/data/testdir"))
print("The absolute path : ", path.abspath(""))



