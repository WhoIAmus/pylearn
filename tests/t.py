n,m = map(int, input().split(" "))
x = sorted(map(int,input().split(" ")), reverse=True)
l,r=x[0]/n,x[0]
while r-l>1e-10:
    m=(l+r)/2
    k=0
    for t in x:
        k+=t//m
        if t//m==0:
            break
    if k<n:
        r=m
    else:
        l=m
print(l)
