# Problem: Find All Good Indices - https://leetcode.com/problems/find-all-good-indices/

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        li = [0] * n
        rd = [0]*n
        li[0] = rd[-1] = 1
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                li[i] += li[i-1] + 1
            else:
                li[i] = 1
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]: 
                rd[i] += rd[i+1] + 1
            else:
                rd[i] = 1
        ans = []
        for i in range(k, n-k):
            if li[i-1] >= k and rd[i+1] >= k:
                ans.append(i)
        return ans
