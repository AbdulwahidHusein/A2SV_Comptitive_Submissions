class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        oddv = False
        for l in c:
            if c[l] % 2 == 0:
                ans += c[l]
            else:
                ans += c[l] - 1
                oddv = True
        return ans + 1 if oddv else ans

