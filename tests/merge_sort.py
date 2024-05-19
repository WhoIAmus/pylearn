def msort(l):
    def inner(left,right):
        nonlocal l
        if left == right:
            return

        inner(left,(left+right)//2)
        inner((left+right)//2+1,right)

        r = [None for _ in range(right-left+1)]
        lp = left
        rp = (left+right)//2+1
        for i in range(right-left+1):
            if lp<=(left+right)//2 and rp<=right:
                if l[lp]<l[rp]:
                    r[i]=l[lp]
                    lp+=1
                else:
                    r[i]=l[rp]
                    rp+=1
            else:
                if lp<=(left+right)//2:
                    r[i]=l[lp]
                    lp+=1
                else:
                    r[i]=l[rp]
                    rp+=1
        l[left:right+1]=r
    
    inner(0,len(l)-1)

l = [1,76,4,79,23,214,65,4423,65658,1,34321,6,6776,234,312,12,5,265]
msort(l)

print(l)
