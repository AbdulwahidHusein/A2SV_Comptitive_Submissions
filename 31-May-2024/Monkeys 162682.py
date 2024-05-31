# Problem: Monkeys - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/E

class DSU:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.count = n
        self.groups = [[i] for i in range(n + 1)]
    def find(self, node):
        if node == self.parent[node]:
            return node

        stack = []
        while node != self.parent[node]:
            stack.append(node)
            node = self.parent[node]

        # Path compression
        for n in stack:
            self.parent[n] = node

        return node

    def Runion(self, u, v):
        rep_u = self.find(u)
        rep_v = self.find(v)
        if rep_u == rep_v:
            return False
        if self.rank[rep_u] < self.rank[rep_v]:
            self.parent[rep_u] = rep_v
        elif self.rank[rep_v] < self.rank[rep_u]:
            self.parent[rep_v] = rep_u
        else:
            self.parent[rep_v] = rep_u
            self.rank[rep_u] += 1
        self.count -= 1

        return True

    def Sunion(self, u, v):
        rep_u = self.find(u)
        rep_v = self.find(v)
        if rep_u == rep_v:
            return
        if self.size[rep_u] < self.size[rep_v]:
            self.parent[rep_u] = rep_v
            self.size[rep_v] += self.size[rep_u]
            self.groups[rep_v].extend(self.groups[rep_u])
        else:
            self.parent[rep_v] = rep_u
            self.size[rep_u] += self.size[rep_v]
            self.groups[rep_u].extend(self.groups[rep_v])
            
from collections import defaultdict
n,m  = map(int, input().split())


lefts = defaultdict(int)
righs = defaultdict(int)

for i in range(n):
    l, r = map(int, input().split())
    if l != -1:
        lefts[i+1] = l
    if r != -1:
        righs[i+1] = r
uf = DSU(n)
releases = []
rld = set()
for _ in range(m):
    id, hnd = list(map(int, input().split()))
    rld.add((id, hnd))
    releases.append((id, hnd))
    
for i in range(n):
    if not (i+1, 1) in rld and lefts[i+1]:
        uf.Sunion(i+1, lefts[i+1])
    if not (i+1, 2) in rld and righs[i+1]:
        uf.Sunion(i+1, righs[i+1])
        

tm = defaultdict(lambda: -1)


time = len(releases) - 1
while releases:
    id, hnd = releases.pop()
    
    relid = lefts[id] if hnd == 1 else righs[id]
    p1 = uf.find(id)
    p2 = uf.find(relid)
    p0 = uf.find(1)
    
    if p1 == p0 and p2 == p0:
        pass
    elif p1 != p0 and p2 != p0:
        pass
    
    elif p1 == p0:
        for mnk in uf.groups[p2]:
            tm[mnk] = time
            
    else:
        for mnk in uf.groups[p1]:
            tm[mnk] = time
    uf.Sunion(p2, p1)
    time -= 1

for i in range(1, n+1):
    print(tm[i])
        