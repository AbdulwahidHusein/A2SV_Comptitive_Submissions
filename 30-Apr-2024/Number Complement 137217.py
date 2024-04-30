# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        for k in range(int(log2(num))+1):
            num ^= (1<<k) 
        return num  