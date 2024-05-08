# Problem: B - tourist orz! - https://codeforces.com/gym/522079/problem/B

for _ in range(int(input())):
    n, z = map(int,input().split())
    nums = list(map(int, input().split()))
    ans = 0
    for m in nums:
        ans = max(ans, z |m)
        
    print(ans)