class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pref_sum = [0]*n

        for start, end in requests:
            pref_sum[start] += 1
            if end < n-1:
                pref_sum[end+1] -= 1
        
        for i in range(1, n):
            pref_sum[i] += pref_sum[i-1]

        nums.sort()
        pref_sum.sort()

        ans = 0
        for i in range(n):
            ans += (nums[i] * pref_sum[i]) 

        return ans % (10**9 + 7)