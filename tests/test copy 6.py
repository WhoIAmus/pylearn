from math import inf

n,m = map(int,input().split())
A = [[0 for i in range(n)] for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    A[a-1][b-1]=A[b-1][a-1]=c

f = [False for i in range(n)]
l = [inf for i in range(n)]
l[0]=0

q = {0}
while len(q)>0:
    t = min(q, key= lambda j: l[j])
    q.remove(t)
    if f[t]:
        continue
    for i in range(n):
        if A[t][i]==0:
            continue
        if l[t]+A[t][i]<l[i]:
            l[i]=l[t]+A[t][i]
            q.add(t)
    f[t]=True

print(l)