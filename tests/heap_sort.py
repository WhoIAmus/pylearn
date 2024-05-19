from math import inf

class Heap():
    def __init__(self):
        self.l = list(inf for _ in range(15))
        self.c = 0

    def check_up(self,ind):
        if ind == 0:
            return
        else:
            if self.l[(ind-1)//2] > self.l[ind]:
                self.l[(ind-1)//2],self.l[ind] = self.l[ind],self.l[(ind-1)//2]
                ind = (ind-1)//2
                self.check_up(ind)

    def check_down(self,ind):
        if ind*2+2 > self.c:
            return
        else:
            if self.l[ind*2+1] > self.l[ind*2+2]:
                nind = ind*2+2
            else:
                nind = ind*2+1

            if self.l[nind] < self.l[ind]:
                self.l[nind],self.l[ind] = self.l[ind],self.l[nind]
                self.check_down(nind)

    def add(self,value):
        if self.c == len(self.l):
            self.l.extend(list(inf for _ in range(len(self.l)+1)))

        self.l[self.c] = value
        self.check_up(self.c)
        self.c+=1

    def remove(self):
        self.l[0] = self.l[self.c-1]
        self.l[self.c-1] = inf
        self.c-=1
        self.check_down(0)

    def top(self):
        return self.l[0]

    def __str__(self):
        return str(self.l)



def heap_sort(l):
    heap = Heap()
    for t in l:
        heap.add(t)
    for i in range(len(l)):
        l[i]=heap.top()
        heap.remove()
    return l

def heap_sort_v2(l):
    c=len(l)-1

    def check_down(ind):
        a,b=ind*2+1,ind*2+2
        m =ind

        if a <= c and l[a]>l[m]:
            m=a

        if b <= c and l[b]>l[m]:
            m=b

        if m!=ind:
            l[m],l[ind]=l[ind],l[m]
            check_down(m)

    for i in range(c,-1,-1):
        check_down(i)

    while c>0:
        l[0],l[c] = l[c],l[0]
        c-=1
        check_down(0)
    
    return l





if __name__ == "__main__":
    import random
    #l = [-5, -4, 7, 0, -6, 9, 5, -7, -1, -9]
    l = [random.randrange(-10,10) for _ in range(10)]
    print(l)
    print('\/')
    print(heap_sort_v2(l))
    print(heap_sort_v2(l) == sorted(l))

        # c = len(l)-s
        # if ind*2+2 > c:
        #     return
        # else:
        #     if l[ind*2+1] > l[ind*2+2]:
        #         nind = ind*2+2
        #     else:
        #         nind = ind*2+1

        #     if l[nind] < l[ind]:
        #         l[nind],l[ind] = l[ind],l[nind]
        #         check_down(nind)