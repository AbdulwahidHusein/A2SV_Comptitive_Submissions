# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        peoples = []
        for i in range(n):
            peoples.append([efficiency[i], speed[i]])
        peoples.sort(reverse = True)
        speed_sum = ans = 0
        heap = []
        for eff, spd in peoples:
            if len(heap) == k:
                speed_sum -=  heappop(heap)
            heappush(heap, spd)
            speed_sum += spd
            ans = max(ans, speed_sum * eff)

        return ans % (10**9+7)


