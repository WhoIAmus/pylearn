l = list(map(int,input().split()))
m=1
k = len(l)
w = 'r'

while m != 0:
    k-=1
    m=0
    if w == 'r':
        for i in range(k):
            if l[i]<=l[i+1]:
                pass
            else:
                l[i],l[i+1]=l[i+1],l[i]
                m+=1
        else:
            for i in range(k-1,-1,-1):
                if l[i]<=l[i-1]:
                    pass
                else:
                    l[i],l[i-1]=l[i-1],l[i]
                    m+=1
print(l)