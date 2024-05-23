# Problem: A - Distribute - https://codeforces.com/gym/524965/problem/A

n = int(input())

nums = [int(i) for i in input().split()]
for i in range(n):
    nums[i] = (nums[i], i)
nums.sort()

for i in range(n//2):
    print(nums[i][1]+1, nums[n-i-1][1]+1)