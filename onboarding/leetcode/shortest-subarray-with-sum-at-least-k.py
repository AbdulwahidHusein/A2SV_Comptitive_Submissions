class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()#indices, sum
        q.append([-1, 0])
        pref = 0
        ans = float('inf')
        for i in range(n):
            pref += nums[i]
            while q and pref - q[0][1] >= k:
                ans = min(ans, i - q.popleft()[0])
            while q and q[-1][1] >= pref:
                q.pop()
            q.append([i, pref])
        return ans if ans != float("inf") else -1
