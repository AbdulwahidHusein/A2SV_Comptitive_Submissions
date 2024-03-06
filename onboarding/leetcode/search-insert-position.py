class Solution:
    def bis(self, n, arr):
            left = 0
            right = len(arr) - 1
            while right >= left:
                middle = (left + right) // 2
                if arr[middle] == n:
                    return middle
                elif arr[middle] > n:
                    right = middle - 1
                else:
                    left = middle + 1
            return left

    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        return self.bis(target, nums)

        