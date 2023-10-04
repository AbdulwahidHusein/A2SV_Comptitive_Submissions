class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        m = len(nums)

        return m*(m+1)//2 - s