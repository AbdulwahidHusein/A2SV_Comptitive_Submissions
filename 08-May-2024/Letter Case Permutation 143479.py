# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        upper = s.upper()
        lower = s.lower()

        letters = 0
        for w in s:
            if w.isalpha():
                letters += 1

        res = []
        
        for i in range(1 << letters): 
            wi = 0
            curr = []
            for j in range(len(s)):
                if s[j].isdigit():
                    curr.append(s[j])
                    wi += 1
                elif (1 << (j - wi)) & i != 0: 
                    curr.append(upper[j])
                else:
                    curr.append(lower[j])
            res.append("".join(curr))
        return res