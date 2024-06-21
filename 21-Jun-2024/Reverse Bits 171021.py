# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int: 
        res = 0
        for i in range(32):
            if (1 << i) & n:
                res |= (1 << (31-i))
        
        return res