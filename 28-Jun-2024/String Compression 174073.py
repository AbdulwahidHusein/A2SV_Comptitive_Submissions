# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, cs: List[str]) -> int:
        idx1 , idx2 = 0, 0
        while idx1 < len(cs):
            c, start = cs[idx1],idx1
            while idx1<len(cs) and cs[idx1] == c:
                idx1+=1
            cs[idx2]= c
            idx2+=1
            count=idx1-start
            if count>1:
                for digit in str(count):
                    cs[idx2]=digit
                    idx2+=1
        return idx2 