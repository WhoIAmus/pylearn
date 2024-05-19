n = int(input())
k = list(input().split())
d = {}

for i in k:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

s=''
d = list(d.items())

for i in d:
    s+=i[0]*(i[1]//2)
next()
y = next(filter(lambda t: t[1]%2!=0,d),("",0))[0]

print(s+y+''.join(list(reversed(s))))
