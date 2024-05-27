# Problem: B - String Fusion - https://codeforces.com/gym/526229/problem/B

from sys import stdin
import sys
input = stdin.readline
class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(26) ]
        self.wc = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        n = len(word)
        word = word[::-1]
        for i, character in enumerate(word):
            idx = ord(character) - ord("a")
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            curr.wc += 1

    def search(self, prefix, root):
        if len(prefix) == 0:
            return 0
        res = 0
        curr = root
        st = [w for w in prefix[::-1]]
        
        while st and curr.children[ord(st[-1]) - ord("a")]:
            res += 2 * curr.children[ord(st[-1]) - ord("a")].wc
            curr = curr.children[ord(st[-1]) - ord("a")]
            st.pop()
        return res


    
trie = Trie()
ans = 0
ww = []
total = 0
n = int(input())
for _ in range(n):
    s = input().strip()
    ww.append(s)
    trie.insert(s)
    total += 2 * len(s) * n
    

for s in ww:
    ans += trie.search(s, trie.root)
    
print( total-ans)