class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        dist1 = 0
        if start < destination:
            for i in range(start, destination):
                dist1 += distance[i]
        else:
             for i in range(destination, start):
                 dist1 += distance[i]
        return min(dist1, sum(distance)-dist1)