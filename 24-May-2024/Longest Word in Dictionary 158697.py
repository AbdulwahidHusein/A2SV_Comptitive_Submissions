# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.end = None

    def insert(self, word: str) -> None:
        curr = self.root
        for character in word:
            idx = ord(character) - ord("a")
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True        

    def search(self, word: str) -> bool:
        return self.startsWith(word) and self.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for character in prefix:
            idx = ord(character) - ord("a")
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
            if not curr.is_end:
                return False
        return curr.is_end
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ans = "{"
        ll = 0
        for word in words:
            if trie.startsWith(word):
                if len(word) > ll:
                    ans = word
                    ll = len(word)
                elif len(word) == ll:
                    ans = min(ans, word)
        return ans if ans != "{" else ""
        