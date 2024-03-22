class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            m = nums[i]
            while m != i + 1 and nums[m-1] != m:
                nums[i], nums[m-1] = nums[m-1], m
                m = nums[i] 
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans = [nums[i], i+1]
        return ans