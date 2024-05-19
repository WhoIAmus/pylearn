import random
typee = list(range(10))

def quicksort(l):
    lp = 0
    rp = len(l)-1

    if len(l) <=1:
        return l
    elif len(l) == 2:
        if l[0] > l[1]:
            l[0],l[1] = l[1],l[0]
        return l

    pivot = 0

    while lp < rp:
        if l[lp] < l[pivot]:
            lp+=1
        elif l[rp] >= l[pivot]:
            rp-=1
        else:
            l[lp],l[rp] = l[rp],l[lp]

    ll = l[:lp]
    rl = l[lp+1:]

    ll = quicksort(ll)
    rl = quicksort(rl)

    l[:lp]=ll
    l[lp+1:]=rl
    
    return l

random.shuffle(typee)
print(quicksort(typee))
