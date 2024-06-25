# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)} # Using dictionary
        self.size = {i:1 for i in range(size)}
        
    def find(self, x):
        if self.parent[x] == x:
            return x
        parent = self.find(self.parent[x])
        self.parent[x] = parent
        return parent
    
    def union(self, x, y):
        rooty = self.find(y)
        rootx = self.find(x)
        if rootx == rooty:
            return
        if self.size[rootx] > self.size[rooty]:
            self.parent[rooty] = rootx
            self.size[rootx] += self.size[rooty]
        else:
            self.parent[rootx] = rooty
            self.size[rooty] += self.size[rootx]

                
    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu  = UnionFind(n)
        for u, v in edges:
            dsu.union(u, v)
        unreachableNodes = n * (n + 1) //2
        for node in range(n):
            if node == dsu.parent[node]:
                size = dsu.size[node]
                unreachableNodes -= size * (size + 1) //2
        return unreachableNodes