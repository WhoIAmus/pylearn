n,k=map(int,input().split())
l=list(map(int,input().split()))

np= list(filter(lambda t: t%2!=0,l))
p= list(filter(lambda t: t%2==0,l))

if len(np)==n and k%2==0:
    print('no')
elif len(p)==n:
    print('no')

else:
    j = list()
    if len(p)>=k-1:
        j.extend(p)
        j.extend(np[0:k-1])
        j=list(map(str,j))
        j1=' '.join(j)
        print(f'yes\n{j1}')
    else:
        j.extend(np[0:len(np) if len(np)%2!=0 else len(np)-1])
        j.extend(p[0:k-len(j)])
        j1=' '.join(j)
        print(f'yes/n{j1}')