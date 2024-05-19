from math import inf

n,m = map(int,input().split())
l = list()

for i in range(n):
    l.append(list(map(int,input().split())))

dist = [inf for i in range()]
s = 0
c = list()
info = set((0,0))

r=0
d=0

while m>0:
    if m-l[d][r]>0:
        r+=1



#info.append((info[0][0]-1,info[0][1]-1))

print(info)
