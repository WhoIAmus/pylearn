import c_sort
import random
from Linked_list_class import List
from math import log

def buket(l):
    maxx = max(l)
    minn = min(l)
    lenn = len(l)-1
    lenn = lenn + 1

    ll = [List() for _ in range(4)]

    for i in l:
        k = int(((i-minn)/(maxx-minn+1))*4)
        ll[k].l_add(i)

    l0 = list(map(lambda t:[None for _ in range(len(t))],ll))

    for k in range(len(ll)):
        for (i,v) in zip(range(len(ll[k])),ll[k]):
            l0[k][i]=v

    c=0
    for t in l0:
        if len(t)>=1:
            l[c:c+len(t)] = c_sort.c_sort(t)
            c+=len(t)
    
    return l
    

if __name__ == '__main__':
    for i in range(200):
        l = [random.randrange(-10,10) for _ in range(10)]
        print(l)
        print('\/')
        if sorted(l) == buket(l):
            print(True)
        print(' ')


