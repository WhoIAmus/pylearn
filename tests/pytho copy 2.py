from math import sqrt
n = int(input())
m = 2

for i in range(2, int(sqrt(n))+1):
    if n%i==0:
        print('no no simp')
        break
else:
    print('yes yes simp') 
