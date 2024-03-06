class Solution:
    def time_it_takes(self, piles, k):
        time = 0
        for i in range(len(piles)):
            time += ceil(piles[i] / k)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        _min = 1
        _max = max(piles)
        mid = (_max + _min) // 2
        while _min <= _max:
            time = self.time_it_takes(piles, mid)
            if time > h:
                _min = mid + 1
            else:
                res = mid
                _max = mid - 1
            mid = (_min + _max) // 2
        return res