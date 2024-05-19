import random
from math import log
def radix_sort(ll,b):
    maxxa = max(ll)
    minna = min(ll)
    def c_sort(l,k):
        L = len(l)
        key = lambda x:((x-minna)//b**k)%b
        minn = key(l[0])
        maxx = key(l[0])

        for i in range(1,L):
            if key(l[i]) < minn:
                minn = key(l[i])
            if key(l[i]) > maxx:
                maxx = key(l[i])

        c = [0 for _ in range(maxx-minn+1)]

        for i in l:
            c[key(i)-minn] += 1

        for i in range(1,len(c)):
            c[i] += c[i-1]

        r = [None for _ in range(L)]

        for i in range(L-1,-1,-1):
            c[key(l[i])-minn]-=1
            r[c[key(l[i])-minn]]=l[i]

        return r

    for _ in range(int(log(maxxa-minna,b))+1):
        ll = c_sort(ll,_)
    return ll

if __name__ == "__main__":
    l = [random.randrange(-999,999) for _ in range(1000)]
    print(radix_sort(l,128))
