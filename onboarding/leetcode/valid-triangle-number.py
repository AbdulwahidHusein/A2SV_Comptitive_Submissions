class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()#lets brute force
        n=len(nums)
        ans = 0
        for k in range(2,n):
            i=0
            j=k-1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    ans+=(j-i)
                    j-=1
                else:
                    i+=1
        return ans 