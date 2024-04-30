# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = defaultdict(int)
        for a, b in edges:
            indegree[b] += 1
        res  =[]
        for y in range(n):
            if indegree[y] == 0:
                res.append(y)
        return res[0] if len(res) == 1 else -1