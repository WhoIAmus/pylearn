a = list(map(int,input().split())) # к-сть рахунків та % відрахування
b = list(map(int,input().split())) # гроші на рахунках
c=0
percent = 1-a[1]/100

d = sorted(b)

while len(d) != 1:
    d.append((d[0]+d[1])*percent)
    
    d.pop(0)
    d.pop(0)


#while len(b)!=1:
#   b[0] = (b[0]+b[1])*percent
#  b.pop(1)

print(d[0])