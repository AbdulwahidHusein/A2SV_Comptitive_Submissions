class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        sum_ = sum(nums)
        for i in range(n-1, -1, -1):
            if sum_ - nums[i] > nums[i]:
                return sum_
            sum_ = sum_ - nums[i]
        return -1