
n,m = map(int,input().split())

l=[[0 for i in range(n)] for i in range(m)]

for i in range(m):
    k,j=map(int,input().split())
    l[i][k-1]=l[i][j-1]=1

g = False

a,b = map(lambda t:int(t)-1,input().split())
for i in range(m):
    if l[i][a] == 1 and l[i][b] == 1:
        g = True
        break

if g == True:
    print('yess')
else:
    print('nono')

print(l)