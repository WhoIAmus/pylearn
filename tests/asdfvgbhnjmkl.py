l = list(map(int,input().split()))
m=1
k = len(l)

while m != 0:
    k-=1
    m=0
    for i in range(k):
        if l[i]<=l[i+1]:
            pass
        else:
            l[i],l[i+1]=l[i+1],l[i]
            m+=1

print(l)