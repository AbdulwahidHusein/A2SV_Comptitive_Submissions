class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1 
        postfix = 1 

        arr = [0 for _ in range(len(nums))] 

        for i in range(len(nums)):
            arr[i] = prefix 
            prefix *= nums[i]

        for j in range(len(nums)-1, -1, -1):
            arr[j] *= postfix
            postfix *= nums[j]

        return arr