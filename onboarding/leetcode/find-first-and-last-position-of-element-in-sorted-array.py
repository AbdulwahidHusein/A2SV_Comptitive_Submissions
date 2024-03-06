class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)

        if right == 0 or left == len(nums) or nums[left] != target or nums[right-1] != target:
            return [-1, -1] 
        return [left, right-1]