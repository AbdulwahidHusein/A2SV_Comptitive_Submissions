# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

# Union Find class
class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)} # Using dictionary
        self.size = {i:1 for i in range(size)}
        self.sum = {i:0 for i in range(size)}
        self.max_segment = 0
    def find(self, x):
        if self.parent[x] == x:
            return x
        parent = self.find(self.parent[x])
        self.parent[x] = parent
        return parent
    def add(self, idx, n):
        parent = self.find(idx)
        self.sum[parent] += n
        self.max_segment = max(self.max_segment, self.sum[parent])

    def union(self, x, y):
        rooty = self.find(y)
        rootx = self.find(x)
        if rootx == rooty:
            return
        if self.size[rootx] > self.size[rooty]:
            self.parent[rooty] = rootx
            self.size[rootx] += self.size[rooty]
            self.sum[rootx] += self.sum[rooty]
            self.max_segment = max(self.max_segment, self.sum[rootx])
        else:
            self.parent[rootx] = rooty
            self.size[rooty] += self.size[rootx]
            self.sum[rooty] += self.sum[rootx]
            self.max_segment = max(self.max_segment, self.sum[rooty])
            
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = UnionFind(n)
        ans = []
        visited = set()
        for i in range(len(removeQueries)-1, -1, -1):
            ans.append(uf.max_segment)
            idx = removeQueries[i]
            uf.add(idx, nums[idx])
            if idx + 1 in visited:
                uf.union(idx, idx+1)
            if idx - 1 in visited:
                uf.union(idx, idx-1)
            visited.add(idx)
        return reversed(ans)

