class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr_pos = nums[0]
        if nums[0] == 0 and n>1:
            return False
        for i in range(1, n):
            if curr_pos <= i and nums[i] == 0 and i < n-1:
                return False
            curr_pos = max(curr_pos, i+nums[i])
        return True