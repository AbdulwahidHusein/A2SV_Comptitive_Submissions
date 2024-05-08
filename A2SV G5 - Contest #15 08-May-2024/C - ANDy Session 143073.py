# Problem: C - ANDy Session - https://codeforces.com/gym/522079/problem/C

def solve():
    n, k = map(int, input().split())
    nums = [int(i) for i in input().split()]
    ones = [0] * 32
    for m in nums:
        for i in range(32):
            if m & (1 << i):
                ones[i] += 1

    full = []
    for i in range(30, -1, -1):
        if ones[i] < n and k >= (n - ones[i]):
                k -= (n - ones[i])
                full.append(i)
                
    ans = nums[0]
    for m in nums:
        ans &= m
    for pos in full:
        ans |= (1 << (pos))
    print(ans)


for _ in range(int(input())):
    solve()