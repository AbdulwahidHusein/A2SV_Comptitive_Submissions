class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n//2):
            for j in range(nums[2*i]):
                ans.append(nums[2*i+1])
        return ans #not efficint just for test