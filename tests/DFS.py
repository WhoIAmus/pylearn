from Linked_list_class import *

n,m = map(int,input().split())
l = [[0 for i in range(n)] for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    l[a-1][b-1]=l[b-1][a-1]=1

N = set()
s = stack()
E = set()
N.add(0)
s.s_push(0)

while len(s) > 0 :
    for i in range(n):
        if l[s.s_top()][i]!=0 and i not in N:
            t = i
            break
    else:
        s.s_pop()
        continue
    E.add((s.s_top(),t))
    s.s_push(t)
    N.add(t)   

print(E)

#BFS: {(0, 1), (0, 2), (0, 3), (1, 4)} vs DFS: {(0, 1), (1, 2), (1, 4), (4, 3)}
