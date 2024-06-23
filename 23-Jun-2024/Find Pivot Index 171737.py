# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0]
        right_sum = [0]
        l = len(nums)
        for i in range(l):
            left_sum.append(left_sum[-1] + nums[i])
            right_sum.append(right_sum[-1]+nums[l-i-1])

        for i in range(1, l+1):
            if left_sum[i] == right_sum[l-i+1]:
                return i-1
        return -1