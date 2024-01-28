class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n =  len(nums)
        s = sum(nums)
        R = s % p
        if R == 0:
            return 0
        pref_sum = [0] * (n+1)
        for i in range(1, n+1):
            pref_sum[i] = pref_sum[i-1] + nums[i-1]

        store = {}
        ans = float('inf')
        for i in range( n+1):
            pmp = pref_sum[i] % p
            if pmp in store:
                ans = min(ans, i-store[pmp])
            m = (R + pmp ) % p
            store[m] = i
        if ans >= n:
            return -1
        return ans
        
