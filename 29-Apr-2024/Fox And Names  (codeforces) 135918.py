# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

n = int(input())
s = []
for _ in range(n):
    s.append(input())

mat = [[0] * 30 for _ in range(30)]
visited = [0] * 30
N = 0
use = [0] * 30
ans = [''] * 30
cycle = False

def build(x, y):
    l1 = len(s[x])
    l2 = len(s[y])
    for i in range(min(l1, l2)):
        if s[x][i] != s[y][i]:
            mat[ord(s[x][i]) - ord('a')][ord(s[y][i]) - ord('a')] = 1
            return True
    return l1 <= l2

def dfs(s):
    global cycle, N
    if visited[s] == 1:
        cycle = True
        return
    if visited[s] == 2:
        return
    visited[s] = 1
    for t in range(26):
        if mat[s][t]:
            dfs(t)
    visited[s] = 2
    ans[N] = chr(s + ord('a'))
    N += 1

for i in range(n - 1):
    if not build(i, i + 1):
        print("Impossible")
        exit(0)

for i in range(26):
    if not visited[i]:
        dfs(i)

if cycle:
    print("Impossible")
else:
    for i in range(N - 1, -1, -1):
        print(ans[i], end='')
        use[ord(ans[i]) - ord('a')] = 1
    for i in range(26):
        if not use[i]:
            print(chr(i + ord('a')), end='')