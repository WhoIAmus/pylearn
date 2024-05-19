n = int(input())

p = [2]

for i in range(3,n):
    for t in p:
        if i%t==0:
            break
    else:
        p.append(i)

print(p)
