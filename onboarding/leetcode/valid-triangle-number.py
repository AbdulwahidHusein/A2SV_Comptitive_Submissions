class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        ans = 0
        for i in range(2, n):
            for j in range(i):
                nedded = nums[i] - nums[j] + 1
                idx = bisect.bisect_left(nums, nedded)
                if idx < j:
                    ans += j - idx
        return ans