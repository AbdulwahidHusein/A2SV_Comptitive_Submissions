class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = (right+left) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]