# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        def is_palin(s):
            return s == s[::-1]
        
        dp = defaultdict(lambda: float("inf"))
        dp[0] = 0
        dp[-1] = -1

        for i in range(1, len(s)):
            for j in range(i, -1, -1):
                if is_palin(s[j:i+1]):
                    dp[i] = min(dp[i], dp[j-1] + 1)

        return dp[len(s)-1]