
class Node():
    def __init__(self,value = None,key = None,left = None,right = None):
        self.left = left
        self.right = right
        self.value = value
        self.key = key

class PriorityQueueTreee():
    def __init__(self):
        self.root = Node()
        self.c = 0

    def enqueue(self, priority, value):
        if self.c == 0:
            self.root.value = value
            self.root.key = priority
            self.root.right = Node()
            self.root.left = Node()
            self.c+=1
        else:
            a = self.root
            while a.left is not None and a.right is not None:
                if priority > a.key:
                    a = a.right
                else:
                    a = a.left
            a.value = value
            a.key = priority
            a.right = Node()
            a.left = Node()
            self.c+=1 

    def remove(self,node:Node):
        t = a = node
        if a.left.left is not None:
            a = a.left
            temp = None
            while a.right.right is not None:
                if a.right.right.right is None:
                    temp = a
                a = a.right
            if temp is not None:
                temp.right = a.left
            else:
                t.left=a.left
            t.key=a.key
            t.value=a.value
        elif a.right.right is not None:
            a = a.right
            temp = None
            while a.left.left is not None:
                if a.left.left.left is None:
                    temp = a
                a = a.left
            if temp is not None:
                temp.left = a.right
            else:
                t.right = a.right
            t.key = a.key
            t.value = a.value
        else:
            t.__init__()

    def f_dequeue(self):
        a = self.root
        while a.left.left is not None:
            a = a.left
        val=a.value
        if a.right.right is None:
            a.__init__()
        else:
            t = a
            a = a.right
            temp = None
            while a.left.left is not None:
                if a.left.left.left is None:
                    temp = a
                a = a.left
            if temp is not None:
                temp.left = a.right
            else:
                t.right = a.right
            t.key = a.key
            t.value = a.value
        return val

    def l_dequeue(self):
        a = self.root
        while a.right.right is not None:
            a = a.right
        val=a.value
        if a.left.left is None:
            a.__init__()
        else:
            t = a
            a = a.left
            temp = None
            while a.right.right is not None:
                if a.right.right.right is None:
                    temp = a
                a = a.right
            if temp is not None:
                temp.right = a.left
            else:
                t.left=a.left
            t.key=a.key
            t.value=a.value
        return val

    def __str__(self):
        def process(root):
            a=""
            if root.left.left is not None:
                a += process(root.left)
            a+=f"({root.key} : {root.value}), "
            if root.right.right is not None:
                a += process(root.right)
            return a
        return "{"+process(self.root)[:-2]+"}"

    def __len__(self):
        return self.c

    def __hash__(self) -> int:
        return sum(map(ord,str(self)))

if __name__=="__main__":
    t = PriorityQueueTreee()
    t.enqueue('b', 9.11)
    t.enqueue('c', 3.1415)
    t.enqueue('d', 56123)
    t.enqueue('e', 76453890)
    t.enqueue('f', 456312797)
    t.enqueue('g', 2)
    t.enqueue('h', 7689)
    print(t.f_dequeue())
    print(t.l_dequeue())
