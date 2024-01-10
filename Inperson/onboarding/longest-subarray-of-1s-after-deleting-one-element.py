class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        k = 1
        ans = 0

        while right < n:
            if nums[right] == 0:
                k-= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            right += 1
            ans = max(ans, right - left)
        return ans - 1
