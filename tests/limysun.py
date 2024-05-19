n,k,x = map(int,input().split())
l = list(map(int,input().split()))

w = 4

for t in l:
    if t > k:
        if x>0:
            x-=1
        else:
            w-=1
    else:
        pass

if w <= 2:
    print('NO')
else:
    print('YES')