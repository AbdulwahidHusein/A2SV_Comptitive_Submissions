class Solution:
    def result(self, nums, divisor):
        ans = 0
        for i in range(len(nums)):
            ans += ceil(nums[i] / divisor)
        return ans
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        _max = sum(nums)
        _min = 1
        while _min <= _max:
            mid = (_min + _max) // 2
            th = self.result(nums, mid)
            if th <= threshold:
                res = mid
                _max = mid - 1
            else:
                _min = mid + 1
        return res
            