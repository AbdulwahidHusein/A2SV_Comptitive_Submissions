class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count = 0
        for i,n in enumerate(nums):
            nums[i] = nums[i] + count
            count = nums[i]
        return nums