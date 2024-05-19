a,b,c = map(int,input().split())

s = set()

if a + b <= 47:
    s.add(True)
else:
    s.add(False)

if b + c <= 47:
    s.add(True)
else: 
    s.add(False)

if a + c <= 47:
    s.add(True)
else: 
    s.add(False)


if True in s:
    print('YES')
else:
    print('NO')