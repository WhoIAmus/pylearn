import random
def c_sort(l):
    L = len(l)

    minn = l[0]
    maxx = l[0]

    for i in range(1,L):
        if l[i] < minn:
            minn = l[i]
        if l[i] > maxx:
            maxx = l[i]

    c = [0 for _ in range(maxx-minn+1)]

    for i in l:
        c[i-minn] += 1

    for i in range(1,len(c)):
        c[i] += c[i-1]

    r = [None for _ in range(L)]

    for i in range(L-1,-1,-1):
        c[l[i]-minn]-=1
        r[c[l[i]-minn]]=l[i]

    return r

if __name__ == '__main__':
    print(c_sort([random.randrange(-10,10) for _ in range(30)]))
