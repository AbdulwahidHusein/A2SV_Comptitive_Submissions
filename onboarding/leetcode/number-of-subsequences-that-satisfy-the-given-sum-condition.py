class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        print(nums)
        ans = 0
        for i in range(n):
            if nums[i] > target:
                continue
            pos = bisect_right(nums, target - nums[i])
            if pos > i:
                ans += 2 ** (pos-i-1)
        return ans % (10**9 + 7)