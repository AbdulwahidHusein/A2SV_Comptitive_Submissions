# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E

n, k = map(int, input().split())
nums = [int(i) for i in input().split()]

ps = []
for i in range(n-1, -1, -1):
    if ps:
        ps.append(ps[-1] + nums[i])
    else:
        ps = [nums[i]]
    

ans = ps.pop()
ps.sort()
for i in range(k-1):
    ans += ps.pop()
    
print(ans)

