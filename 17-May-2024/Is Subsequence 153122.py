# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        sp = 0
        tp = 0

        while tp < len(t):
            if s[sp] == t[tp]:
                sp+=1
                if sp == len(s):
                    return True
            tp += 1
        return False