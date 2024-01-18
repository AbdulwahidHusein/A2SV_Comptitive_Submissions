class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        pref_sum = [0]*(n+1)
        c = Counter()
        ans = 0
        c[goal] = 1
        for i in range(1, n+1):
            pref_sum[i] += nums[i-1] + pref_sum[i-1]
            if c[pref_sum[i]] > 0:
                ans += c[pref_sum[i]]
            c[goal+pref_sum[i]] += 1
            
        return ans