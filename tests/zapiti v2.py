n,m = map(int,input().split())
l = list(map(int,input().split()))

memo = {}



def add(i,d):
    l[i-1]+=d

def summ(f,t):
    if (f,t) in memo:
        return memo[(f,t)]
    
    memo[(f,t)]=sum(l[f-1:t])
    
    return sum(l[f-1:t])
