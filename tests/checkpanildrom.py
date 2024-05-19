s = input()

se = set(list(s))
n=len(s)
f=False
for i in range(n//2):
    if s[i]!=s[n-1-i]:
        f=True
        break
if f:
    print(n)
elif len(se)==1:
    print(-1)
else:
    print(n-1)
