from math import *
a = int(input())
l = list()
print(log2(a))
for i in range(1,ceil(sqrt(a))):
    if a%i == 0:
        l.append(i)
        
print(l)