# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for j in range(n):
                if nums[j] <= i:
                    dp[i] += dp[i - nums[j]]

        return dp[-1]

        