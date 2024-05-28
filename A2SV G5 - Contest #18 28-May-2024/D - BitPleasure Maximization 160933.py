# Problem: D - BitPleasure Maximization - https://codeforces.com/gym/526229/problem/D

import sys
input = sys.stdin.readline
class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(2) ]
        self.right = float('-inf')

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.end = None

    def insert(self, n, ix):
        curr = self.root
        for j in range(63, -1, -1):
            idx = int((n & (1 << j)) > 0)
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            curr.right = max(curr.right, ix)

    def search(self, n, ix):
        curr = self.root
        ans = 0
        for i in range(63, -1, -1):
            idx = 1 - int((n & (1 << i)) > 0)
            if curr.children[idx] and curr.right > ix:
                curr = curr.children[idx]
                ans |= (1 << i)
            elif curr.children[1 - idx]:
                curr = curr.children[1 - idx]
            else:
                return ans
        return ans



trie = Trie()
n = int(input())

trie.insert(0, n)

nms = [int(i) for i in input().split()]
xorp = []

lxor = 0

rxor = 0
trie.insert(0, n)
for i in range(n-1, -1, -1):
    rxor ^= nms[i]
    trie.insert(rxor, i)
    
    
ans = 0
for i in range(n):
    lxor ^= nms[i]
    ans = max(ans, trie.search(lxor, i))
    
ans = max(ans, trie.search(0, -1))
print(ans)