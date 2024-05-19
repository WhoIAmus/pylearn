l = list(map(int,input().split()))
k = len(l)

for i in range(k):
    g=i
    for t in range(i,k):
        if l[t]<l[g]:
            g=t

    l[g],l[i]=l[i],l[g]

print(l)