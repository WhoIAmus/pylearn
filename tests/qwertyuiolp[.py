class Node:
    def __init__(self,pointer = None,value = None):
        self.value = value
        self.pointer = pointer

class queue:
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
            raise Exception('nothin to delete, dumb')
        self.c-=1
        v = self._head.pointer.value
        self._head.pointer = self._head.pointer.pointer
        return v

    def __len__(self):
        return self.c

n,m = map(int,input().split())
l = [[0 for i in range(n)] for i in range(n)]

fromm,too = map(int,input().split()) 

for i in range(m):
    a,b = map(int,input().split())
    l[a-1][b-1] = l[b-1][a-1] = 1

def bfs(fm,to):
    N = set()
    q = queue()
    prev = [-1 for _ in range(n)]
    lenght = [0 for _ in range(n)]
    tl = []
    N.add(fm)
    q.enqueue(fm)
    while len(q) > 0 :
        for i in range(n):
            if l[q.head()][i]!=0 and i not in N:
                t = i
                break
        else:
            q.dequeue()
            continue
        prev[t]=q.head()
        lenght[t]=1+lenght[q.head()]
        if(t==to):
            tl.append(lenght[t])
            l[t][q.head()]=l[q.head()][t]=0
        else:
            q.enqueue(t)
            N.add(t)
    return int(tl.count(min(tl))%(1e9+7))

print(bfs(fromm-1,too-1))
