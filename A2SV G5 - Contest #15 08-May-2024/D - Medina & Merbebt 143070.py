# Problem: D - Medina & Merbebt - https://codeforces.com/gym/522079/problem/D

from sys import stdin

input = stdin.readline
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    pref = [[0] * 30 for _ in range(n + 1)]
    for i in range(n):
        for j in range(30):
            if a[i] & (1 << j):
                pref[i + 1][j] = pref[i][j] + 1
            else:
                pref[i + 1][j] = pref[i][j]
    q = int(input())
    res = []
    for _ in range(q):
        l, k = map(int, input().split())
        if a[l - 1] < k:
            res.append(-1)
            continue
        _min = l
        _max = n
        ans = l
        while _min <= _max:
            s = (_min + _max) // 2
            num = 0
            for j in range(30):
                if pref[s][j] - pref[l - 1][j] == s - l + 1:
                    num += (1 << j)
            if num >= k:
                _min = s + 1
                ans = max(ans, s)
            else:
                _max = s - 1
        res.append(ans)
    print(*res)

t = int(input())
for _ in range(t):
    solve()