#import sys
from sys import *
print("Before Exit")
#sys.exit(0)

x=100
print("The size of x is " , getsizeof(x))
print("The recursion limit ", getrecursionlimit())

setrecursionlimit(10)



