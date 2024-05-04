# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a
        mask = 0xFFFFFFFF  
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        if a & (1 << 31):  
            a = ~(a ^ mask)
        return a