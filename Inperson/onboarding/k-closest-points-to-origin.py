class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_distance = [0]*(len(points))
        i= 0
        for x, y in points:
            point_distance[i] = [(x, y), x**2 + y**2]
            i += 1
        
        point_distance.sort(key = lambda item: item[1])
        ans = [0]*k
        for i in range(k):
            ans[i] = point_distance[i][0]
        return ans