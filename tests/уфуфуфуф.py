
a=list(map(int,input().split()))
b=list(map(int,input().split()))

t = 0
l = 0

if len(a)>len(b):
    for i in range(len(a)):
        if a[i]==b[l]:
            t+=1
            l+=1
        else:
            pass

    if t == len(b):
        print('yes')
    else:
        print('no')

elif len(a)==len(b):
    if a == b:
        print('yes')
    else:
        print('no')

elif len(a)<len(b):
    print('no')