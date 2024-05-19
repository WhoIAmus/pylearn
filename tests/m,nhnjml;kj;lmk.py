from Linked_list_class import *

n,m = map(int,input().split())
l = [[0 for i in range(n)] for i in range(n)]

fromm,too = map(int,input().split()) 

for i in range(m):
    a,b = map(int,input().split())
    l[a-1][b-1] = l[b-1][a-1] = 1



def bfs(fm,to):
    N = set()
    q = queue()
    prev = [None for _ in range(n)]
    N.add(fm)
    q.enqueue(fm)
    while len(q) > 0 :
        for i in range(to):
            if l[q.head()][i]!=0 and i not in N:
                t = i
                break
        else:
            q.dequeue()
            continue
        prev[t]=q.head()
        q.enqueue(t)
        N.add(t)
    return prev

print(bfs(fromm,too))
