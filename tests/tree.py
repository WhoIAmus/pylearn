
class Node():
    def __init__(self,value = None,key = None,left = None,right = None):
        self.left = left
        self.right = right
        self.value = value
        self.key = key

class Tree():
    def __init__(self):
        self.root = Node()
        self.c = 0

    def set(self, key, value):
        if self.c == 0:
            self.root.value = value
            self.root.key = key
            self.root.right = Node()
            self.root.left = Node()
            self.c+=1
            self.was = False
        else:
            a = self.root
            while a.left is not None and a.right is not None:
                if key == a.key:
                    a.value = value
                    return
                elif key > a.key:
                    a = a.right
                else:
                    a = a.left
            a.value = value
            a.key = key
            a.right = Node()
            a.left = Node()
            self.c+=1 

    def get(self, key):
        a = self.root
        while a.key != key:
            if a.right is None and a.left is None:
                raise KeyError(f"There is no object with \"{key}\" key in the Tree")
            if key > a.key:
                a = a.right
            else:
                a = a.left
        return a.value

    def remove(self,key):
        a = self.root
        while a.key != key:
            if a.right is None and a.left is None:
                raise KeyError(f"There is no object with \"{key}\" key in the Tree")
            if key > a.key:
                a = a.right
            else:
                a = a.left
        t = a

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

    def __iter__(self):
        def walk(root):
            if root.left.left is not None:
                yield from walk(root.left)
            yield (root.key, root.value)
            if root.right.right is not None:
                yield from walk(root.right)
        yield from walk(self.root)

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,value):
        self.set(key,value)

    def __len__(self):
        return self.c

    def __hash__(self) -> int:
        return sum(map(ord,str(self)))

if __name__=="__main__":
    t = Tree()
    t["a"]=1
    t.set('g', 9.11)
    t.set('b', 3.1415)
    for i in t:
        print(i)
