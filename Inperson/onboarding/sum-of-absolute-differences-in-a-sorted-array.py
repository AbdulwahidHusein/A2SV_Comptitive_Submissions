class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        lps=[0]
        rps =[0]*len(nums)
        n = len(nums)
        for i in range(1, n):
            lps.append(lps[i-1] +( nums[i] - nums[i-1])*i)
        
        for i in range(n-2, -1, -1):
            rps[i] = rps[i+1] + (nums[i+1] - nums[i] ) * (n-1-i)

        for i in range(n):
            lps[i] += rps[i]

        return lps