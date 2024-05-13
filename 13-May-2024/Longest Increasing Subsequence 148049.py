# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)
        visited = set()
        def dp(idx):
            if idx in visited:
                return memo[idx]
            y = 0
            for i in range(idx-1, -1, -1):
                if nums[i] < nums[idx]:
                    y = max(y, dp(i))
            memo[idx] = y + 1
            visited.add(idx)
            return memo[idx]
        for i in range(len(nums)):
            dp(i) 
        return max(memo)
