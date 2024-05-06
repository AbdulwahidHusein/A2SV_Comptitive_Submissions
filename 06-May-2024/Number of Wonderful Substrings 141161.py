# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = defaultdict(int)
        count[0] = 1
        ans = 0
        ps = 0
        for i, ch in enumerate(word):
            for w in ch:
                ps ^=  1 << (ord(w) - ord('a'))
            ans += count[ps]
            for i in range(10):
                ans += count[ps ^ (1 << i)]
            count[ps] += 1            
        return ans