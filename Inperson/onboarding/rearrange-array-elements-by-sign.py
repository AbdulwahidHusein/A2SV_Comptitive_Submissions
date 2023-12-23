class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        neg = 0
        pos = 0
        ans = [0]*n
        i = 0
        while neg < n and pos < n:
            if nums[neg] >= 0:
                neg += 1
            if nums[pos] < 0:
                pos += 1
            if nums[neg] < 0 and nums[pos] >= 0:
                ans[i] = nums[pos]
                ans[i+1] = nums[neg]
                i+=2
                neg += 1
                pos += 1
        return ans