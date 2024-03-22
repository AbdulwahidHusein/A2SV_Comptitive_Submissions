class Solution:
    def cycleSort(self, arr):
        for i in range(len(arr)):
            m = arr[i] 
            while m != i and arr[m] != m:
                arr[i], arr[m] = arr[m], m
                m = arr[i]
        return arr
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return int(not nums[0])
        for i in range(n):
            if nums[i] == n:
                if i > 0:
                    nums[i] = nums[i-1]
                else:
                    nums[i] = nums[i+1]
        s = self.cycleSort(nums)
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return n
         