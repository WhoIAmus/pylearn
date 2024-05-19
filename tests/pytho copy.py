l = list(map(int,input().split()))
m = 1

while m !=0:
    m=0
    for i in range(len(l)-1):
        p = i
        if l[p]>l[p+1]:
            j = l[p]
            m+=1
            while True:
                if p == 0:
                    break
                elif j<l[p+1] and j>l[p-1]:
                    break
                else:
                    l[p],l[p-1]=l[p-1],l[p]
                    p-=1

print(l)
