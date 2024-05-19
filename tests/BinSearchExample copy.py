from math import *

r,h = map(int,input().split())
top = r + h

def p(x):
     y = -mid/sqrt((r**2)-(mid**2))
     return y

def f(x):
     y = sqrt(r**2-x**2)
     return y

tol = 1e-6

left = 0

right = r

while right-left>tol:
    mid = (left+right)/2
    y = -mid*p(mid)+f(mid)
    if y > top:
         right = mid
    else:
         left = mid

print(2*pi*r*(r-f((right + left)/2)))
