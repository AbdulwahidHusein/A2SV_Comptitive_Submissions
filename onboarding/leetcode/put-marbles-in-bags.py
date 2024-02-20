class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        adj = []
        for i in range(1, n):
            adj.append(weights[i] + weights[i-1])
        adj.sort()
        return sum(adj[n - k :]) - sum(adj[:k-1])