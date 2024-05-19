h,c = map(int,input().split())
l = list()

for i in range(h):
    l.append(list(map(int,input().split())))

x = len(l[0])-1
y = 0

while True:
    if x==0 and y==len(l) and l[y][x]!=c:
        print('no')
        break
    elif l[y][x]==c:
        print('yes')
        break
    elif l[y][x]>c:
        x-=1
    else:
        y+=1
