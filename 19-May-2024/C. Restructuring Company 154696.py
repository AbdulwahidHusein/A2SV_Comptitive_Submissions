# Problem: C. Restructuring Company - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C

from sys import stdin
input = stdin.readline
class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(1, 1+size)}
        self.size = {i:1 for i in range(1, 1+size)}
    def find(self, x):
        stack = [x]
        while self.parent[x] != x:
            x = self.parent[x]
            stack.append(x)
        for i in stack:
            self.parent[i] = x
        return x
    
    def union(self, x, y):
        rooty = self.find(y)
        rootx = self.find(x)
        if rootx == rooty:
            return
        if self.size[rootx] > self.size[rooty]:
            self.parent[rooty] = rootx
            self.size[rootx] += self.size[rooty]
        else:
            self.parent[rooty] = rootx
            self.size[rooty] += self.size[rootx]
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

n, q = map(int, input().split())
uf = UnionFind(n)
_next = [i for i in range(1, n+5)]

for _ in range(q):
    t,x,y = map(int, input().split())
    if t == 3:
        if uf.is_connected(x, y):
            print("YES")
        else:
            print("NO")
    elif t == 1:
        uf.union(x, y)
    else:
        par = uf.find(y)
        
        while x <= y:
            uf.union(x, par)
            curr = x
            x = _next[x]
            _next[curr] = _next[y]
            