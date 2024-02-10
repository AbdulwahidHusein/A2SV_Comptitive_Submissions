class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref_sum = 0
        c = Counter()
        c[k] = 1
        ans = 0
        for i in range(1, n+1):
            pref_sum += nums[i-1]
            if c[pref_sum] > 0:
                ans += c[pref_sum]
            c[pref_sum+k] += 1

        return ans