class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        candidates = self.store[key]
        n = len(candidates)
        ridx = bisect_right(candidates, timestamp, key = lambda x: x[0])
        if ridx == 0:
            return ""
        return candidates[ridx-1][1]
    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)