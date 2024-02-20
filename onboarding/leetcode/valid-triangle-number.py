class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()#lets brute force
        n=len(nums)
        ans = 0
        for i in range(2,n):
            left=0
            right=i-1
            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    ans+=(right-left)
                    right-=1
                else:
                    left+=1
        return ans 