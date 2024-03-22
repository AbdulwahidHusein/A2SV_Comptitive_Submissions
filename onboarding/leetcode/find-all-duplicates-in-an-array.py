class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            m = nums[i]
            while m != i + 1 and nums[m-1] != m:
                nums[i], nums[m-1] = nums[m-1], m
                m = nums[i] 
        ans = set()
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.add(nums[i])
        return list(ans)