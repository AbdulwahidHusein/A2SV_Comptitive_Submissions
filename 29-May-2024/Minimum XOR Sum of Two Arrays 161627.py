# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        # ans = float(inf)

        # @cache
        # def backtrack(idx, mask, xor):
        #     nonlocal ans
        #     if idx == len(nums1):
        #         ans = min(ans, xor)
            
        #     for i in range(len(nums1)):
        #         if not (1 << i ) & mask:
        #             mask |= (1 << i)
        #             xor += nums1[idx] ^ nums2[i]
        #             if xor < ans:
        #                 backtrack(idx+1, mask, xor)
        #             xor -= nums1[idx] ^ nums2[i]
        #             mask &= ~(1 << i)
        # backtrack(0, 0, 0)
        # return ans    

        @cache
        def dp(idx, mask):
            if idx == len(nums1):
                return 0
            ans = float("inf")
            for i in range(len(nums2)):
                if not (1 << i ) & mask:
                    mask |= (1 << i)
                    ans = min(ans, dp(idx+1,mask) + (nums1[idx] ^ nums2[i]))
                    mask &= ~(1 << i)
            return ans

        return dp(0, 0)