# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(2) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(31, -1, -1): 
            idx = int( ((1 << i) & word) > 0)
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True        


    def max_similarity(self, prefix: str) -> bool:
        l = 0
        curr = self.root
        for i in range(31, -1, -1):
            idx = 1 - int( ((1 << i) & prefix) > 0) 
            if curr.children[idx]: 
                curr = curr.children[idx]
                l |= (1 << i)
            elif curr.children[1-idx]:
                curr = curr.children[1-idx]
            else:
                return l
        return l

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        nums.reverse()
        trie = Trie()

        ans = 0
        for n in nums:
            trie.insert(n)
            ans = max(ans, trie.max_similarity(n))
        return ans


        