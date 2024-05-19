a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

if len(a)>len(c) and len(a)>len(b):
    m = len(a)
elif len(b)>len(c) and len(b)>len(a):
    m = len(b)
else:
    m = len(c)

i1=0
i2=0
i3=0

try:
    while True:
        if a[i1]==b[i2] and b[i2]==c[i3]:
            print(a[i1])
            break
        elif a[i1] > b[i2] and a[i1] > c[i3]:
            i2+=1
            i3+=1
        elif a[i1] > b[i2] and a[i1] < c[i3]:
            i1+=1
            i2+=1
        elif a[i1]<b[i2] and a[i1] < c[i3]:
            i1+=1
        elif a[i1]==b[i2] and a[i1]<c[i3]:
            i1+=1
            i2+=1
        elif a[i1]==c[i3] and a[i1]<b[i2]:
            i1+=1
            i3+=1
        elif c[i3]==b[i2] and c[i3]<a[i1]:
            i2+=1
            i3+=1
        elif a[i1]==b[i2] and a[i1]>c[i3]:
            i3+=1
        elif a[i1]==c[i3] and a[i1]>b[i2]:
            i2+=1
        elif c[i3]==b[i2] and c[i3]>a[i1]:
            i1+=1
        
except:
    print(None)
