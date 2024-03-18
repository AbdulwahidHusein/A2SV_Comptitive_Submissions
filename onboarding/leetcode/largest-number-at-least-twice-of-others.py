class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx = max(nums)
        for i in range(len(nums)):
            if nums[i] == mx:
                continue
            if 2*nums[i] > mx:
                return -1
        return nums.index(mx)