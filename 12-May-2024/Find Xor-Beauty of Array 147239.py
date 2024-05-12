# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        bv = [0] * 32
    
        shifts = [1<<i for i in range(32)]
        for m in nums:
            for i in range(32):
                if m & shifts[i] != 0: 
                    bv[i] += 1
        
        ans = 0
        for i in range(32):
            if bv[i] * 3 * bv[i] * bv[i] % 2 != 0:
                ans |= (1 << i)
        return ans
            