class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        exist = n + 1
        for i in range(n):
            if nums[i] > 0 and nums[i] <= n:
                exist = nums[i]
        if exist == n+1:
            return 1
        for i in range(n):
            if nums[i] > n or nums[i] <= 0:
                nums[i] = exist
        for i in range(n):
            r = nums[i]
            while r != i+1 and nums[r-1] != r:
                nums[i], nums[r-1] = nums[r-1], nums[i]
                r = nums[i]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n + 1