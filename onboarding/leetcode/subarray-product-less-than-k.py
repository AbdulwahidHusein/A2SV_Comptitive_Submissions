class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        n = len(nums)
        pr = 1
        ans = 0
        left = 0
        for right in range(n):
            pr *= nums[right]
            while pr >= k and left <= right:
                pr /= nums[left] 
                left += 1
            ans += right - left + 1
            right += 1
        return ans
 