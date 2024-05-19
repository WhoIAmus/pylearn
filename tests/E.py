import sys
from math import gcd

# Define constants
MAX_N = 200005
MAX_K = 6000011
INF = 1000111222

# Define global variables
mn = [0] * MAX_K
a = [0] * MAX_N
l = [0] * MAX_N
r = [0] * MAX_N
n = 0
q = 0
ans = [0] * MAX_N
d = [[] for _ in range(MAX_K)]
pp = [0] * MAX_K
have = [[] for _ in range(MAX_N)]
add = [[] for _ in range(MAX_N)]
pref = [0] * MAX_N
qq = [[] for _ in range(MAX_N)]

# Define fenwick tree class
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.t = [0] * n

    def update(self, i, x):
        while i < self.n:
            self.t[i] = max(self.t[i], x)
            i |= i + 1

    def query(self, r):
        ans = 0
        while r >= 0:
            ans = max(ans, self.t[r])
            r = (r & (r + 1)) - 1
        return ans

# Define functions
def solve():
    for i in range(q):
        qq[l[i]].append(i)

    for i in range(n):
        x = a[i]
        while x > 1:
            y = mn[x]
            cnt = 0
            while x % y == 0:
                x //= y
                cnt += 1
            d[y].append([(i, cnt), (n + 1, n + 1)])

        pref[i] = a[i] + (pref[i - 1] if i > 0 else 0)

    Q = []
    for i in range(2, MAX_K):
        if not d[i]:
            continue
        for j in range(len(d[i]) - 1, -1, -1):
            if j + 1 < len(d[i]) and d[i][j][0][0] + 1 == d[i][j + 1][0][0]:
                d[i][j][1][0] = d[i][j + 1][1][0]
            else:
                d[i][j][1][0] = d[i][j][0][0] + 1

            while Q and d[i][Q[-1]][0][1] >= d[i][j][0][1]:
                Q.pop()

            if Q:
                d[i][j][1][1] = Q[-1]
            Q.append(j)

        Q.clear()

    def get_sum(l, r):
        return pref[r] - pref[l - 1] if l > 0 else pref[r]

    for i in range(n):
        have[i].append((i, a[i]))
        while have[i]:
            L, g = have[i].pop()
            to = n
            G = g
            while g > 1:
                y = mn[g]
                cnt = 0
                while g % y == 0:
                    g //= y
                    cnt += 1

                pos = pp[y]
                while pos < len(d[y]) and d[y][pos][0][0] < i:
                    pos += 1

                if pos < len(d[y]) and d[y][pos][0][0] == i:
                    while pos < len(d[y]) and d[y][pos][0][1] >= cnt:
                        pos = d[y][pos][1][1]
                    if pos >= len(d[y]):
                        pos = len(d[y]) - 1
                    else:
                        pos -= 1
                    now = max(i + 1, d[y][pos][0][0] + 1)
                    now = min(now, d[y][pp[y]][1][0])
                else:
                    now = i + 1

                to = min(to, now)
                pp[y] = pos

            if to < n:
                assert G != gcd(G, a[to])
                have[to].append((L, gcd(G, a[to])))
            add[L].append((to - 1, G))

    T = Fenwick(n)

    def update(R, val):
        while R >= 0:
            T.update(R, val)
            R = (R & (R + 1)) - 1

    def query(R):
        ans = 0
        while R < n:
            ans = max(ans, T.query(R))
            R |= R + 1
        return ans

    for i in range(n - 1, -1, -1):
        for j in add[i]:
            update(j[0], j[1] * get_sum(i, j[0]))

        for j in qq[i]:
            R = r[j]
            s = get_sum(i, R)
            G = -1
            for k in add[i]:
                if k[0] >= R:
                    G = k[1]
                    break
            assert G != -1
            ans[j] = max(ans[j], s * G)
            ans[j] = max(ans[j], query(R))

# Main function
def main():
    global n, q

    for i in range(2, MAX_K):
        if not mn[i]:
            for j in range(i, MAX_K, i):
                if not mn[j]:
                    mn[j] = i

    debug = 0

    if not debug:
        n, q = map(int, input().split())
    else:
        n = q = 5

    a = list(map(int, input().split())) if not debug else [randint(1, 10) for _ in range(n)]

    for i in range(q):
        l[i], r[i] = map(int, input().split())
        l[i] -= 1
        r[i] -= 1

    solve()

    for i in range(q):
        l[i], r[i] = n - 1 - r[i], n - 1 - l[i]

    a.reverse()
    solve()

    a.reverse()
    for i in range(q):
        l[i], r[i] = n - 1 - r[i], n - 1 - l[i]

    for i in range(q):
        print(ans[i])

        if debug:
            pass  # Add debug logic here

if __name__ == "__main__":
    main()
