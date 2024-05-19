n,m = map(int,input().split())
l = list(map(int,input().split()))
memo = {}

def add(i,d):
    l[i-1]+=d

def update():
 pass
def summ(f,t):
    if (f,t) in memo:
        return memo[(f,t)]
    
    memo[(f,t)]=sum(l[f-1:t])

for g in range(m):
    h = list(map(int,input().split()))
    if h[0] == 1:
        if len(h)==3:
            print(summ(h[1],h[2]))
        else:
            print(l[h[1]])
    else:
        add(h[1],h[2])
