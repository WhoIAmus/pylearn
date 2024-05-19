from math import pi

n,m = map(int,input().split())
ballz = []
for i in range(m):
    v = (4/3)*pi*(int(input())**3)
    ballz.append(v)

sballz = sorted(ballz,reverse=True)
tol = 1e-4

right = sballz[0]
left = sballz[0]/n

while right-left > tol:
    mid = (right+left)/2
    s = 0
    for i in sballz:
        s+=i//mid
        if i//mid == 0:
            break
    if s>=n:
        left = mid
    else:
        right = mid

print(((right+left)/2)*n)