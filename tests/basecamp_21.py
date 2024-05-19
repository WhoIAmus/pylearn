from math import ceil

n, k = list(map(int,input().split(" ")))
a = list(map(int,input().split(" ")))
k=1-k/100

sorted(a)

while n>1:
    for i in range(n//2+1):
        a[i]=(a[i]+a[n-(i+1)])*k
    n=int(ceil(n/2))
print(a[0])