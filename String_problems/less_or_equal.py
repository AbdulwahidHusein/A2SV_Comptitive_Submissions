def less_or_equals(nums, k):
    nums.sort()
    if k > len(nums):
        print(-1)
        return
    target = nums[k-1]
    count = nums.count(target)
    if count >= k:
        print(target)
    else:
        
        
        print(target + 1)

n, k = map(int, input().split())
nums = [int(i) for i in input().split()]
less_or_equals(nums, k)