class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key = lambda x: x[0])
        arrows  = 0
        min_right = points[0][1]
        for i in range(1, n):
            if points[i][0] > min_right:
                min_right = points[i][1]
                arrows += 1
            min_right = min(min_right, points[i][1] )
        return arrows+1

        #1,6   2,8,  7,12,   10,16