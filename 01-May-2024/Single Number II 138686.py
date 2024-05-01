# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0 for _ in range(32)]
        ncounts = [0 for _ in range(32)]
        for n in nums:
            neg = False
            if n < 0:
                n = ~n + 1
                neg = True
            for i in range(32):
                y = 1 << i & n
                if y != 0:
                    counts[i] += 1
                    if neg:
                        ncounts[i] += 1
        res = 0
        negative = False
        for i in range(32):
            if counts[i] % 3 != 0:
                if ncounts[i] % 3 != 0:
                    negative = True
                res |= 1 << i
        return res if not negative else -res