from math import inf

class Node:
    def __init__(self,pointer = None,value = None):
        self.value = value
        self.pointer = pointer

class TNode:
    def __init__(self,lpointer = None, value = None, rpointer = None):
        self.value = value
        self.rpointer = rpointer
        self.lpointer = lpointer

class List:
    def __init__(self):
        self.first = Node()
        self.c = 0
        self.last = self.first

    def l_add(self,value):
        self.last.value = value
        self.last.pointer = Node()
        self.last=self.last.pointer
        self.c+=1

    def __str__(self):
        a = self.first
        s = "["
        while a.pointer is not None:
            if a.pointer.value is None:
                s+=str(a.value)+"]"
                a = a.pointer
            else:
                s+=str(a.value)+", "
                a = a.pointer
        return s

    def __len__(self):
        return self.c

    def l_del(self,target):
        a = self.first
        while a.pointer is not None and a.pointer.value != target:
            a = a.pointer
        if a.value is not None:
            a.pointer = a.pointer.pointer

    def __iter__(self):
        a = self.first
        while a.pointer is not None:
            yield a.value
            a=a.pointer

    def extend(self,lst):
        if lst is not self:
            self.last.pointer = lst.first.pointer
            self.last.value = lst.first.value
            self.c+=lst.c
        else:
            raise KeyError('fk you, infinite loop ERROR404')

    def minn(self):
        if self.c == 0:
            print('add something, you dumb.')
        else:
            m = inf
            a = self.first
            while a.pointer is not None:
                if a.value < m:
                    m = a.value
                    a = a.pointer
                else:
                    a = a.pointer
            return m

    def maxx(self):
        if self.c == 0:
            print('add something, you dumb')
        else:
            m = -inf
            a = self.first
            while a.pointer is not None:
                if a.value > m:
                    m = a.value
                    a = a.pointer
                else:
                    a = a.pointer
            return m

    def fbigger(self,t):
        if self.c == 0:
            print('add something, you dumb')

        else:
            a = self.first
            while a.pointer is not None:
                if a.value > t:
                    return a.value
                else:
                    a = a.pointer

class stack:
    def __init__(self):
        self.c = 0
        self.top = None

    def s_push(self,value):
        t = Node(pointer=self.top,value=value)
        self.top = t
        self.c+=1

    def __str__(self):
        a = self.top
        s = ""
        while a is not None:
            s+=str(a.value)+" "
            a = a.pointer
        return s

    def s_pop(self):
        if self.top is None:
            raise KeyError('the stack is empty bro, add something, stupid')
        else:
            j = self.top.value
            self.top=self.top.pointer
            self.c-=1
            return j

    def s_top(self):
        return self.top.value

    def __len__(self):
        return self.c

class queue():
    def __init__(self):
        self._head = self._tail = Node()
        self.c = 0

    def enqueue(self,value):
        self._tail.pointer = Node(value = value)
        self._tail=self._tail.pointer
        self.c+=1

    def __str__(self):
        a = self._head.pointer
        s = ""
        while a is not None:
            s+=str(a.value)+" "
            a = a.pointer
        return s

    def head(self):
        return self._head.pointer.value

    def tail(self):
        return self._tail.value

    def dequeue(self):
        if self.c == 0:

            raise KeyError('nothin to delete, dumb')
        self.c-=1
        v = self._head.pointer.value
        self._head.pointer = self._head.pointer.pointer
        return v

    def __len__(self):
        return self.c

class p_queue:
    def __init__(self):
        self.head = TNode()
        self.c = 0
        self.tail = self.head

    def enqueue(self,priority,value):
        if self.c == 0:
            self.head.value=(priority,value)
            self.c+=1
            return

        if priority<self.head.value[0]:
            self.head=TNode(None,(priority,value),self.head)
            self.head.rpointer.lpointer=self.head
            self.c+=1
        else:
            a = self.head
            while a.rpointer is not None and a.rpointer.value[0] < priority:
                a = a.rpointer
            t = TNode(a,(priority,value),a.rpointer)
            a.rpointer = t
            self.c+=1
            if t.rpointer is not None:
                t.rpointer.lpointer = t
            else:
                self.tail = t

    def __str__(self):
        a = self.head
        s = "["
        while a is not None:
            if a.rpointer is None:
                s+=str(a.value)+"]"
                a = a.rpointer
            else:
                s+=str(a.value)+", "
                a = a.rpointer
        return s

    def __len__(self):
        return self.c
    
    def f_dequeue(self):
        a = self.head
        self.head = self.head.rpointer
        self.head.lpointer = None
        self.c-=1
        return a.value
    
    def l_dequeue(self):
        a = self.tail
        self.tail = self.tail.lpointer
        self.tail.rpointer = None
        self.c-=1
        return a.value












#sp = p_queue()
#l = [1,4,3,7,9,6,4,3,5,6,4,3,1,4,2,3,4,5,4,3,0]
#for i in l:
#    sp.enqueue(i,i)

#p = p_queue()
#p.enqueue(1,'a')
#p.enqueue(3,'b')
#p.enqueue(4,'c')
#p.enqueue(2,'d')
#p.enqueue(0,'e')
#print(p.l_dequeue())

#stak = stack()
#stak.s_push(1)
#stak.s_push(2)
#stak.s_push(3)
#stak.s_pop()
#stak.s_push(8)

#l = List()
#l.l_add(1)
#l.l_add(2)
#l.l_add(3)
#l.l_add(4)
#print(l.fbigger(1))

##pdr = List()
#pdr.l_add(1)
#pdr.l_add(2)
#pdr.l_add(3)
#pdr.l_add(4)
#pdr.l_add(5)

#print(sp)