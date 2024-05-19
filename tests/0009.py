n,m=map(int,input().split())
l = list(map(set,range(n)))

for i in range(m):
    a,b = map(int,input().split())
    for t in l:
        if t == None:
            continue

print()