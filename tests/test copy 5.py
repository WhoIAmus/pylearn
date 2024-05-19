from math import *

n = int(input())

def func(x):
    s = 0
    for i in range(1,n+1):
        s += asin((i/x)/2)
    return s


def rad(a,b,tol):
    while (b-a)>tol:
        i = (a+b)/2
        if pi>func(i):
            b=i
        else:
            a=i
    return (b+a)/2

print(rad(n/2,75,1e-5))