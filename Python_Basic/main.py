import numpy
'''
Strings
'''
str = "It is String"
b = "Hello, World!"
#Slicing
print(b[2:5])
print(b[:5])
#Negative Indexing
print(b[-13:-8])
#Uppercase
print(b.upper())
print(b.lower())
#Remove whitespace
c = " Hello, World "
print(c.strip())
'''
Use negative indexes to start the slice from the end of the string:
'''
def printString(a, b):
    print(a + b)

def myfunc():
    global x

x = "fantastic"
print("Python is " + x)

"""
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
"""
listcar = ["Hyundai", "KIA", "Honda"] # Lists are used to store multiple items in a single variable.
print(listcar[0])
listnumber = [1,2,3,4,5]
arraynum = numpy.array(listnumber)
print("arraynum[0]:", arraynum[0])
'''
Number
'''
calculation_to_units = 24*60*60
print(f"20 days are {20*calculation_to_units}")
