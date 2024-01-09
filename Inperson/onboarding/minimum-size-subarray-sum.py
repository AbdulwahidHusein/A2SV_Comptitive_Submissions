class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        max_len = float('inf')
        curr_sum = 0
        while right < len(nums):
            curr_sum += nums[right]
            right += 1
            while curr_sum >= target:
                curr_sum -= nums[left]
                left += 1
                max_len = min(max_len, right - left+1)
        return 0 if max_len == float('inf') else max_len