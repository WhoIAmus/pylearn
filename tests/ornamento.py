h,w = map(int,input().split())

for t in range(h):
    for i in range(w):
        if i==t%(w-1) or w-1-i==t%(w-1):
            print("x",end='')
        else:
            print(".",end="")
    print()