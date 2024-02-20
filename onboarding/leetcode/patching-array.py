class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        m = len(nums)
        reach = 0
        insert = 0
        i = 0
        while reach < n:
            if i < m and nums[i] <= (reach+1):
                reach += nums[i]
                i += 1
            else:
                insert += 1
                reach += reach+1
        return insert