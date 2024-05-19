a = list(map(int,input().split()))
b = list(map(int,input().split()))

la = 0
lb = 0
lc = 0
c = [None]*(len(a)+len(b))

while lc<len(c):
    if la == len(a):
        for i in range(len(b)-lb):
            c[lc]=b[lb]
            lc+=1
            lb+=1
    elif lb == len(b):
        for i in range(len(a)-la):
            c[lc]=b[la]
            lc+=1
            la+=1
    else:
        if a[la] >= b[lb]:
            c[lc] = b[lb]
            lc+=1
            lb+=1
        else:
            c[lc]=a[la]
            lc+=1
            la+=1

print(c)