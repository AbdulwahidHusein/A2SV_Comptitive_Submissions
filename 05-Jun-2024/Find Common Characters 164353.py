# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = set(words[0])
        for word in words:
            s = s.intersection(word)
        if s:
            res = []
            for ll in s:
                mc = 1000
                for w in words:
                    mc = min(mc, w.count(ll))
                
                for _ in range(mc):
                    res.append(ll)
            return res
        return []
        