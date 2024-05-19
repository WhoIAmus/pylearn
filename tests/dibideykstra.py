from pqueue_tree import *
from math import inf

n,m = map(int,input().split())
L = [[0 for i in range(n)] for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    L[a-1][b-1]=L[b-1][a-1]=c

N = set()
q = PriorityQueueTreee()
E = set()
N.add(0)
q.enqueue(0,0)

l = [inf for i in range(n)]
l[0]=0
while len(q) > 0 :
    current = q.f_dequeue()
    for i in range(n):
        if L[current][i]!=0 and i not in N:
            l[i]=l[current]=L[current][i]
            E.add((current,i))
            q.enqueue(l[i],i)
    N.add(current)

print(E)

