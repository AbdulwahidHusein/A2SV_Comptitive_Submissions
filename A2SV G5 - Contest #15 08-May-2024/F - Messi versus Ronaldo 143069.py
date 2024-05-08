# Problem: F - Messi versus Ronaldo - https://codeforces.com/gym/522079/problem/F

import sys
input = sys.stdin.readline
def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    
    
    bv = [0] * 60
    
    shifts = [1<<i for i in range(60)]
    
    for m in nums:
        for i in range(60):
            if m & shifts[i] != 0:
                bv[i] += 1
    ans = 0
    mod = 10**9+7
    for m in nums:
        and_sum, or_sum = 0,0
        for i in range(60):
            if  m & shifts[i]!= 0:
                and_sum += shifts[i]* (bv[i])
                or_sum += shifts[i]* n
            else:
                or_sum += shifts[i]* bv[i]
        ans += ((or_sum % mod) * (and_sum % mod)) % mod

    print(ans % mod)
for _ in range(int(input())):
    solve()