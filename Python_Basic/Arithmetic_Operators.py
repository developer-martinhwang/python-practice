'''
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
'''
a = 2
b = 3
result = []
result.insert(0, a+b)
result.insert(1, a-b)
result.insert(2, a*b)
for i in result:
    print(i)