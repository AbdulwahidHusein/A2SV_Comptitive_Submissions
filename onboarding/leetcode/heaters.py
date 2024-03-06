class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = float('-inf')
        for house_pos in houses:
            pos = bisect_left(heaters, house_pos)
            if pos < len(heaters) and heaters[pos] == house_pos: 
                continue
            rad1 = abs(house_pos - heaters[pos-1])
            rad2 = float('inf')
            if pos < len(heaters):
                rad2 = abs(house_pos - heaters[pos])
            ans = max(ans, min(rad1, rad2))
        return ans if ans != float("-inf") else 0