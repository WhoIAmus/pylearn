n,x = map(int,input().split())
s = 0
l = list(map(int,input().split()))
l = sorted(l, reverse=True)

for i in l:
     if i >=10:
          s+=1
     if i <= 9 and x >= 0 and x-(10-i)>=0:
          x-=10-i
          s+=1

print(s)
