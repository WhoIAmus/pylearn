from Linked_list_class import *

n,m = map(int,input().split())
L = [[0 for i in range(n)] for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    L[a-1][b-1]=L[b-1][a-1]=1

N = set()
q = queue()
E = set()
N.add(0)
q.enqueue(0)

while len(q) > 0 :
    for i in range(n):
        if L[q.head()][i]!=0 and i not in N:
            t = i
            break
    else:
        q.dequeue()
        continue
    E.add((q.head(),t))
    q.enqueue(t)
    N.add(t)   

print(E)

