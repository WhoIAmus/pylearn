import random
class Node():
    def __init__(self,value = None,left = None,right = None):
        self.left = left
        self.right = right
        self.value = value

    def insert(self,value):
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = Node(value = value)
        else:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = Node(value = value)

    def arb(self,f):
        if self.left is not None:
            self.left.arb(f)
        f(self.value)
        if self.right is not None:
            self.right.arb(f)

def mysort(l):
    r = [None for _ in range(len(l))]
    random.shuffle(l)
    root = Node(value = l[0])
    for i in range(1,len(l)):
        root.insert(l[i])
    i = 0
    def fun(x):
        nonlocal i
        r[i] = x
        i+=1
    root.arb(fun)
    return(r)

if __name__ == "__main__":
    lisst = [1,4,6,5,3,1,5,6,2,1,67,7,8,7,5,8,0,5,4,3]
    print(mysort(lisst))
