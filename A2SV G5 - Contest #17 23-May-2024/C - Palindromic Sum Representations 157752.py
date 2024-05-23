# Problem: C - Palindromic Sum Representations - https://codeforces.com/gym/524965/problem/C

def is_pas(n):
    return str(n) == str(n)[::-1]
m = 40001
mod = 10 ** 9 + 7
dp = [0 for _ in range(m)]
dp[0] = 1

for i in range(1, m):
    if str(i) == str(i)[::-1]:
        for j in range(1, m):
            if j >= i:
                dp[j] += dp[j - i]
                dp[j] %= mod
            

def solve():
    n = int(input())
    print(dp[n] %mod)
    
for _ in range(int(input())):
    solve()