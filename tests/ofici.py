w=list(map(int,input().split()))
n=list(map(lambda t: bool(int(t)-1),input().split()))
def ssum(f):
    return sum(map(lambda t:t[0],filter(lambda t:t[1]==f,zip(w,n))))
m=max(ssum(False),ssum(True))
s=list()
for i in range(4):
    n[i]=not n[i]
    s.append(max(ssum(False),ssum(True)))
    n[i]=not n[i]

if m<=min(s):
    print(-1)
else:
    print(s.index(min(s))+1)