class Node:
    def __init__(self,value = None,pointer = None):
        self.value = value
        self.pointer = pointer

class hash_table():
    def __init__(self,size):
        self.table = [None for _ in range(size)]
        self.c = size
        self.am = 0

    def add(self, key, value):
        ind = hash_table.myhash1(key)%self.c
        if self.table[ind] is None:
            self.table[ind] = Node((key,value))
        
        else:
            a = self.table[ind]
            while a.pointer is not None:
                a = a.pointer
            a.pointer = Node((key,value),None)
        
        self.am+=1
        if self.am == self.c:
            self.resize(self.c*2)

    @staticmethod
    def myhash1(key):
        t = str(key)
        a = 0
        for i in t:
            a+=ord(i)
        return ((a*149)%139)*137

    @staticmethod
    def myhash2(key):
        t = str(key)
        a = 0
        for i in range(len(t)):
            a+=ord(t[i])*(i+1)
        return a

    @staticmethod
    def myhash3(key):
        t = str(key)
        a = 0
        for i in range(len(t)):
            a += ord(t[i])+(i+1)
        return a

    def __getitem__(self,key):
        ind = hash_table.myhash1(key)%self.c
        a = self.table[ind]
        while a.pointer is not None and a.value[0] != key:
            a=a.pointer
        if a.value[0] == key:
            return self.table[ind][1]
        else:
            return None

    def resize(self,size2):
        old = self.table
        self.c = size2
        self.am=0
        self.table = [None for _ in range(size2)]
        for t in old:
            while t is not None:
                self.add(t.value[0],t.value[1])
                t=t.pointer

    def __setitem__(self,key,value):
        self.add(value,key)

    def __str__(self):
        l = [None for _ in range(self.am)]
        i=0
        for t in self.table:
                while t is not None:
                    l[i] = t.value
                    i+=1
                    t=t.pointer
        return str(l)

    def __delitem__(self,key):
        ind = hash_table.myhash1(key)%self.c
        a = self.table[ind]
        
        if a == None:
            return None
        
        if a.pointer is None and a.value[0] != key:
            return None
        
        if a.value[0] == key:
            self.table[ind]=a.pointer
            self.am -=1
            return

        while a.pointer.pointer is not None and a.pointer.value[0] != key:
            a = a.pointer

        if a.pointer.value[0] == key:
            a.pointer=a.pointer.pointer
            self.am -= 1








if __name__ == "__main__":
    j = hash_table(5)
    j.add('ab','chupakabra')
    j.add('ba','koza')
    j.add('c','bararn')
    j.add('d','korow')
    j.add('e','salo')
    del j['c']
    #j.add('kghjyuhkljumjuhujhyuyhiuhj','hdjasl')
    
    print(j)
