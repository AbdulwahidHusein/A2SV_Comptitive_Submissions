class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = [0]*(n+1)
        ones = [0]*(n+1)
        for i in range(1, n+1):
            if nums[i-1] == 0:
                zeros[i] += zeros[i-1] + 1
            else:
                zeros[i] = zeros[i-1]
        for j in range(n-1, -1, -1):
            if nums[j] == 1:
                ones[j] = ones[j+1] + 1
            else:
                ones[j] = ones[j+1]
        curr_max = max([m+n for (m, n) in zip(ones, zeros)])
        ans = []
        for i in range(n+1):
            if ones[i] + zeros[i] == curr_max:
                ans.append(i)
        return ans
    
        