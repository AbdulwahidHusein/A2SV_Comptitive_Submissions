class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies):
            return max(cookies)
        srtd = sorted(cookies, reverse = True)
        max_perk = sum(srtd[:len(cookies)-k+1])
        ans = float("inf")
        s = sum(cookies)
        def dfs(dist, start, _sum):
            nonlocal ans, max_perk
            if start == len(cookies) and  _sum == s:
                ans = min(ans, max(dist))
                return

            for i in range(start, len(cookies)):
                for j in range(k):
                    if dist[j] < max_perk:
                        dist[j] += cookies[i]
                        _sum += cookies[i]
                        dfs(dist, i+1, _sum)
                        dist[j] -= cookies[i]
                        _sum -= cookies[i]
        dist = [0] * k
        dfs(dist, 0, 0)
        return ans