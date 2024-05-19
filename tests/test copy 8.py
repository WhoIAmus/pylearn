n,m = map(int,input().split())
length = list(map(int,input().split()))
remain = sorted(length, reverse=True)

left = 0
right = remain[0]
tol = 1e-10

while right-left > tol:
    mid = (right+left)/2
    s = 0
    for i in remain:
        s+=i//mid
        if i//mid == 0:
            break
    if s<n:
        right = mid
    else:
        left = mid

print((right+left)/2)
#4 3      
#1 4 2
#1.1875