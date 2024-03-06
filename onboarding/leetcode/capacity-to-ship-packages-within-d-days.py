class Solution:
    def days(self, capacity, weights):
        day = 0
        n = len(weights)
        s = 0
        for i in range(n):
            if s + weights[i] <= capacity:
                s += weights[i]
            else:
                day += 1
                s = weights[i]
        if s:
            day += 1
        return day
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        _min = max(weights)
        _max = sum(weights)

        while _min <= _max:
            mid = (_min + _max) // 2
            d = self.days(mid, weights)
            if d > days:
                _min = mid + 1
            else:
                _max = mid - 1
                res = mid
        return res 