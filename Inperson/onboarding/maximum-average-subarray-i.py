class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        max_av = -float('inf')
        curr_sum = 0
        while right < len(nums):
            curr_sum += nums[right]
            if right-left+1 == k:
                av = curr_sum/(right-left+1)
                max_av = max(max_av, av)
                curr_sum -= nums[left]
                left += 1
            right += 1
            

        return max_av
        

