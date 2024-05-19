from math import inf
class hash_table():
    def __init__(self,size):
        self.table = [None for _ in range(size)]
        self.c = size
        self.am = 0

    def add(self, key, value):
        t = hash_table.myhash(key)
        t = t%self.c
        for i in range(self.c):
            if self.table[(t+i)%self.c] is None or self.table[(t+i)%self.c] == 0:
                self.table[(t+i)%self.c] = (key,value)
                self.am += 1
                break
        if self.am == self.c:
            self.resize(self.c*2)

    @staticmethod
    def myhash1(key):
        t = str(key)
        a = 0
        for i in t:
            a+=ord(i)
        return a

    def __getitem__(self,key):
        ind = hash_table.myhash(key)
        for i in range(self.c):
            if self.table[(ind+i)%self.c] is None:
                return None
            if self.table[(ind+i)%self.c][0] == key:
                return self.table[(ind+i)%self.c][1]

    def resize(self,size2):
        old = self.table
        self.c = size2
        self.am=0
        self.table = [None for _ in range(size2)]
        for t in old:
            if t is not None or t != 0:
                self.add(t[1],t[0])

    def __setitem__(self,key,value):
        self.add(value,key)

    def __str__(self):
        return str(self.table)

    def __delitem__(self,key):
        ind = hash_table.myhash(key)
        for i in range(self.c):
            if self.table[(ind+i)%self.c] is None:
                return
            if self.table[(ind+i)%self.c][0] == key:
                self.table[(ind+i)%self.c]=0
                self.am -= 1
                return







if __name__ == "__main__":
    j = hash_table(5)
    j.add('ab','chupakabra')
    j.add('ba','koza')
    j.add('c','bararn')
    j.add('d','korow')
    j.add('e','salo')
    del j["ab"]
    #j.add('kghjyuhkljumjuhujhyuyhiuhj','hdjasl')
    j.add('ab','chupakabra')
    print(j)
