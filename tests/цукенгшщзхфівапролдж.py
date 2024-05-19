
n,m = map(int,input().split())

l = [[0 for i in range(n)] for i in range(n)]

for i in range(m):
    k,j=map(int,input().split())
    l[k-1][j-1]=1
    l[j-1][k-1]=1

a,b = map(int,input().split())

if l[a-1][b-1] == 1 or l[b-1][a-1] == 1:
    print('yeaahhh')
else:
    print('nuh uh')

print(l)