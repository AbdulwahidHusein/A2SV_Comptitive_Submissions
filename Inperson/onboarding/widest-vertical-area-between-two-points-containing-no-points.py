class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        n = len(points)
        i = 1
        ans = -float("inf")
        while i<n:
            ans = max(points[i][0] - points[i-1][0], ans)
            i += 1
        return ans