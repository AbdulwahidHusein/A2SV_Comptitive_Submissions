# Problem: X-Sum - https://codeforces.com/contest/1676/problem/D

from sys import stdin
input = stdin.readline
def diagonal_sum(i, j, mt, n,m):
    _sum = 0
    _sum += mt[i][j]
    a,b = i, j
    while i < n-1 and j < m-1:
        i += 1
        j += 1
        _sum += mt[i][j]
    i, j = a, b
    while a < n -1 and b > 0:
        a += 1
        b -= 1
        _sum += mt[a][b]
    a, b = i, j
    while i > 0 and j < m-1:
        i -= 1
        j += 1
        _sum += mt[i][j]
    while a > 0 and b > 0:
        a -= 1
        b -= 1
        _sum += mt[a][b]
    return _sum
        
def solve():
    n, m   = map(int, input().split())
    ans = 0
    mt = []
    for _ in range(n):
        mt.append(list(map(int, input().split())))
        
    for i in range(n):
        for j in range(m):
             _sum =  diagonal_sum(i, j, mt, n, m)
             ans = max(ans, _sum)
    print(ans)

for _ in range(int(input())):
    solve()