# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palin(s):
            return s == s[::-1]
        
        dp = defaultdict(list)
        dp[-1] = [[]]
        dp[0] = [[s[0]]]

        for i in range(1, len(s)):
            for j in range(i, -1, -1):
                if is_palin(s[j:i+1]):
                    for k in dp[j-1]:
                        dp[i].append(k + [s[j:i+1]])

        return dp[len(s)-1]
        #abccba