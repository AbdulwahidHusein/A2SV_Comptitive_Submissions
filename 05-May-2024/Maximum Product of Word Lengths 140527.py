# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def build_byte(word):
            chars = 0
            for j in range(len(word)):
                chars |= (1 << (ord(word[j])+1 - ord("a")))
            return chars

        n  = len(words)
        size = [0] * n
        for i in range(n):
            ss = set(words[i])
            size[i] = len(words[i])
            words[i] = [j for j in ss]

        ans = 0
        for i in range(n):
            byte = build_byte(words[i])
            for j in range(i+1, n):  
                byte2 = build_byte(words[j])
                if byte & byte2 == 0:
                    ans = max(ans, size[i] *size[j])
        return ans
            