# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res = []
        xor = 0
        for n in nums:
            xor ^= n
            mask = 0
            for i in range(maximumBit):
                if (1 << i) & xor == 0:
                    mask |= (1 << i)
            res.append(mask)

        return reversed(res)