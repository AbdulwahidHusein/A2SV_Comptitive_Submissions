class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        target = nums[-1]
        n = len(nums)
        ans = 0
        for i in range(n-1, -1, -1):
            if nums[i] > target:
                ans += ceil(nums[i] / target) - 1
                target = nums[i] // (ceil(nums[i] / target))
            else:
                target = nums[i]
        return ans