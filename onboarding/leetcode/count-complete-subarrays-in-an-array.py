class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        #increase right by 1
        # #move left as fas ar possible and incr answer
        def is_eq(original_dc, window_dc):
            return len(original_dc) == len(window_dc)
            
        original_dc = {c:1 for c in nums}
        s = set(nums)
        k = len(s)
        n = len(nums)
        ans = 1
        if k == 1:
            return n*(n+1)//2
        for i in range(n-k):
            c = defaultdict(int)
            left = 0
            right = k+i
            for j in range(right):
                c[nums[j]] += 1
            if is_eq(original_dc, c):
                ans += 1
            while right < n:
                c[nums[left]] -= 1
                if c[nums[left]] < 1:
                    del c[nums[left]]
                c[nums[right]] += 1
                left += 1
                right += 1
                if is_eq(original_dc, c):
                    ans += 1
                
        return ans
            
