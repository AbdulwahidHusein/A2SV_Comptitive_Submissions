class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros = 0
        ones = 0
        twos = 0
        for n in nums:
            if n == 0:
                zeros += 1
            elif n ==1:
                ones += 1
            else:
                twos += 1
        for i in range(len(nums)):
            if zeros:
                nums[i] = 0
                zeros -= 1
            elif ones:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2
        """
        Do not return anything, modify nums in-place instead.
        """
        