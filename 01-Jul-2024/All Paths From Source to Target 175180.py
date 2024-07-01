# Problem: All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for i in range(len(graph)):
            for n in graph[i]:
                adj[i].append(n)

        ans = []
        def backtrack(node, path):
            path.append(node)
            if node == len(graph)-1:
                ans.append(path[:])
                return
            for ng in adj[node]:
                backtrack(ng, path[:])
        backtrack(0, [])

        return ans