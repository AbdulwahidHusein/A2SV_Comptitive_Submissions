# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = nums[0]
        neg = False
        for i in range(1, len(nums)):
            xor ^= nums[i]
        on = 1
        while xor:
            if on & xor:
                break
            on = on << 1
        n1 = 0
        for n in nums:
            if n & on:
                n1 ^= n#filter
        n2 = n1 ^ xor

        return [n1, n2]
        