a =list(map(int,list(input())))
f = sorted(a,reverse=True)
b = sorted(a)
if b[0]==0:
    t = next(filter(lambda t: t!=0,b))
    b[b.index(t)] = 0
    b[0] = t
    
b = list(map(str,b))
f = list(map(str,f))

print(''.join(b)+ ' ' + ''.join(f))
