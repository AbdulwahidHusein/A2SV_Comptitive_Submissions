class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        for i in range(1,n):
            self.nums[i] += self.nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.nums[right] - self.nums[left-1]
        else:
            return self.nums[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)