class hash_table():
    def __init__(self,size):
        self.table = [None for _ in range(size)]
        self.c = size
        self.am = 0

    def add(self, key, value):
        for hash in [hash_table.myhash1, hash_table.myhash2, hash_table.myhash3]:
            t = hash(key)%self.c
            if self.table[t] is None:
                self.table[t] = (key,value)
                self.am += 1
                break
        else:
            t = self.table[hash_table.myhash1(key)%self.c]
            self.table[hash_table.myhash1(key)%self.c] = (key,value)
            self.add(t[0],t[1])
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
        for hash in [hash_table.myhash1, hash_table.myhash2, hash_table.myhash3]:
            ind = hash(key)%self.c
            if self.table[ind][0] == key:
                return self.table[ind][1]

    def resize(self,size2):
        old = self.table
        self.c = size2
        self.am=0
        self.table = [None for _ in range(size2)]
        for t in old:
            if t is not None or t != 0:
                self.add(t[0],t[1])

    def __setitem__(self,key,value):
        self.add(value,key)

    def __str__(self):
        return str(self.table)

    def __delitem__(self,key):
        for hash in [hash_table.myhash1, hash_table.myhash2, hash_table.myhash3]:
            ind = hash(key)%self.c
            if self.table[ind][0] == key:
                self.table[ind]=None
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
    
    print(j["c"])
