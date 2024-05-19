from math import pi

n, m = map(int, input().split(" "))
x = []
for i in range(m):
    t=int(input())
    x.append(pi*t*t*t*4/3)
x = sorted(x, reverse=True)
l,r=x[0]/n,x[0]
while r-l>1e-4:
    m=(l+r)/2
    k=0
    for t in x:
        k+=t//m
        if t//m==0:
            break
    if k<n:
        r=m
    else:
        l=m
print(l*n)
