# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        #sliding window

        n = len(s)
        left = right = 0

        ans = -1
        curr_cost = 0

        for right in range(n):
            curr_cost += abs(ord(s[right]) - ord(t[right]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left)
        
        return ans+1  if ans != -1 else 0
