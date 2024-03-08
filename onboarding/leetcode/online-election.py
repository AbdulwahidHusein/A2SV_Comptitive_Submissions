class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.winners = []
        count = defaultdict(int)
        _max = persons[0]
        for i in range(len(persons)):
            count[persons[i]] += 1
            pi = persons[i]
            if count[pi] >= count[_max]:
                self.winners.append(pi)
                _max = pi
            else:
                self.winners.append(_max)

    def q(self, t: int) -> int:
        idx = bisect_left(self.times, t)
        if len(self.times) == idx or t!=self.times[idx]:
            idx -= 1
        return self.winners[idx]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)