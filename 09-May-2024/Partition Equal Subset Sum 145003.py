# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 != 0:
            return False
        s //= 2
        def can_sum_tabulate(nums, s):
            n = len(nums)
            dp = [[False] * (s+1) for _ in range(n+1)]

            for i in range(n+1):
                dp[i][0] = True
            for i in range(1, n+1):
                for j in range(1, s+1):
                    can =  dp[i-1][j]
                    if j >= nums[i-1]:
                        can = can or dp[i-1][j - nums[i-1]]
                    if can:
                        dp[i][j] = True
                        
            return dp[-1][-1]
        return can_sum_tabulate(nums, s)