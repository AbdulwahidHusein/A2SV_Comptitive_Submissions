class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = deque()
        time = 0
        for i in range(n):
            queue.append((tickets[i], i))
        while queue:
            n = queue.popleft()
            if n[0] - 1 > 0:
                queue.append((n[0]-1, n[1]))
            time += 1
            if n[1] == k and n[0] == 1:
                return time
            