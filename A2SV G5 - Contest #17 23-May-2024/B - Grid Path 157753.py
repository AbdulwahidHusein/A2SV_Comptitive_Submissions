# Problem: B - Grid Path - https://codeforces.com/gym/524965/problem/B

for _ in range(int(input())):
    n,m, k = map(int, input().split())
    
    if m - 1 + m * (n-1) == k:
        print("YES")
    else:
        print("NO")