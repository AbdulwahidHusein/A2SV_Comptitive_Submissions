class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        pairs = 0
        n = len(nums)
        start = 0
        left = 0
        while start < n-1:
            i = start + 1
            while i < n and nums[i] + nums[start] < target:
                i += 1
            pairs += i - start - 1
            start += 1
        return pairs


        # -1 1 1 2 3

