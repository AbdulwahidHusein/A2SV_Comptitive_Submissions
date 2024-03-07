class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        pos = {}
        n = len(intervals)
        for i in range(len(intervals)):
            pos[intervals[i][0]] = i
        intervals.sort()
        ans = [-1] * n

        for i in range(n):
            if intervals[i][0] == intervals[i][1]:
                ans[pos[intervals[i][0]]] = pos[intervals[i][0]]
                continue
            idx = bisect_right(intervals, [intervals[i][1], intervals[i][0]])
            if idx != n:
                ans[pos[intervals[i][0]]] = pos[intervals[idx][0]] 
        return ans