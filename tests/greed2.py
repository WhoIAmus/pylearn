n,k = map(int,input().split())
l = list(map(int,input().split()))
s=0
l = sorted(l)

for i in range(n-k):
    s+=l[i]
    l.pop(i)

print(s)