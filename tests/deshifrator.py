a = input()
a = list(a)
b=''
l = list()

for i in range(len(a)):
    if a[i].isnumeric():
        l.append(a[i])
    else:
        l.append(a[i])
        if len(l) >2:
            l[0] = int(l[0]+l[1])
            l.pop(1)
        b += int(l[0]) * l[1]
        l.clear()


print(b)
