class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s, ans = 0, 0
        for i in range(len(nums)):
            s += nums[i]
            ans = max(ans, (s + i) // (i + 1))
        return ans