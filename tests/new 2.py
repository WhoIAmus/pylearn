from math import *
m=list(map(int,input().split()))
l=list()
for i in range (10):
    if m[i]>0:
        for t in range(m[i]):
            l.append(l)

def summ(x):
    o = []
    for i in range(len(l)):
        for t in range(i,len(l)):
            o.append(str(x[i])+str(x[t]))
    return sum(map(int,o))

d = dict()

for i in range(len(l)):
    h = ' '.join(map(str,l))
    if h in d:
        continue
    else:
        d[h]=summ(l)
        l[i],l[i-1]=l[i-1],l[i]

d[' '.join(map (str, sorted(l, reverse=True)))]-sum(sorted(1, reverse=True))

print(max(d))