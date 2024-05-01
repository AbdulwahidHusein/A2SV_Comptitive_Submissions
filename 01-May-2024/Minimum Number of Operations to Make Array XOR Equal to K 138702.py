# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for n in nums:
            xor ^= n
        ops = 0
        for i in range(32):
            if (xor >> i) & 1 != (k >> i) & 1:
                ops += 1
        return ops