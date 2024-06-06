# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        #1 1 1 0 1 0 1
        #
        n = len(s)
        target = n-1
        ans = 0
        for i in range(n-1, -1, -1):
            if s[i] == '1':
                ans += target - i
                target -= 1
        return ans

