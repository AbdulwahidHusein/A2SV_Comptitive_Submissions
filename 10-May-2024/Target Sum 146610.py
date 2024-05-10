# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n,ans = len(nums), 0
        cache = {}
        def numberOfWays(sm, idx):
            nonlocal n
            if idx == n:
                if sm == target:
                    return 1
                return 0
            if (sm , idx) not in cache:
                cache[(sm, idx)] = numberOfWays(sm + nums[idx], idx+1) + numberOfWays(sm - nums[idx], idx + 1) 
            return cache[(sm, idx)]

        return numberOfWays(0,0)