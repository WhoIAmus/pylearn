b = input()
aim = input()

variants = set()


dic = {'A':'','B':'','C':'','D':''}
for i in range(16):
    l = []
    dic['D'] = bool(i%2)
    dic['C'] = bool((i//2)%2)
    dic['B'] = bool((i//4)%2)
    dic['A'] = bool((i//8)%2)

    for i in b:
        if dic[i]==1:
            l.append(i)
        dic[i]= not dic[i]
    string = "".join(l)
    variants.add(string)

if aim in variants:
    print('Yes')
else:
    print('No')
