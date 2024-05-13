# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(n):
            l = []
            y = 0
            while n:
                y = y*10 + n%10
                n //= 10
            return y
        s = set(nums)
        for n in nums:
            s.add(reverse(n))
        return len(s)
