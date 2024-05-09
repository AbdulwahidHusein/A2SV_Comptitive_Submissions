# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = [-1] * len(nums)
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        def dp(i):
            if memo[i] != -1:
                return memo[i]
            memo[i] =  max(dp(i-2) + nums[i], dp(i-1))
            return memo[i]  
        return dp(len(nums)-1)  