# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

x = int(input())
ans = 0
for i in range(32):
    if (1 << i) & x != 0:
        ans += 1
print(ans)