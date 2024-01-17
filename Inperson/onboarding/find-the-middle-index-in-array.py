class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = [0]*(n+1)
        right_sum = [0]*(n+1)

        for i in range(1,n+1):
            left_sum[i] += nums[i-1] + left_sum[i-1]
        
        right_sum[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            right_sum[i] += right_sum[i+1] + nums[i+1]
        
        for i in range(n):
            if left_sum[i] ==  right_sum[i]:
                return i
        return -1