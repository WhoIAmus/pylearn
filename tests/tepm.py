n,k = map(int,input().split())
a,b = map(int,input().split())

if a>b:
    a,b=b,a

l=0
r=n
tol = 1

while r-l>tol:
    mid = int((l+r)/2)
    if a+(mid*k)-(n-mid)*k<=b:
        l=mid
    else:
        r=mid

s=set()
if a+(l*k)-(n-l)*k<=b:
    s.add(b-(l*k))
    s.add(a+(l*k))
if a+(r*k)-(n-r)*k<=b:
    s.add(b-(r*k))
    s.add(a+(r*k))
print(max(s),min(s))
