class Solution:
    def get_partitions(self, nums, mid):
        pt = 1
        s = nums[0]
        for i in range(1, len(nums)):
            if s + nums[i] > mid:
                pt += 1
                s = nums[i]
            else:
                s += nums[i]

        return pt

    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        _min = max(nums)
        _max = sum(nums)

        while _min <= _max:
            mid = (_min + _max) // 2
            part = self.get_partitions(nums, mid)
            if part > k:
                _min= mid + 1
            else:
                res = mid
                _max = mid - 1
        return res