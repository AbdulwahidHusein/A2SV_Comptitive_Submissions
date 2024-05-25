# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for character in word:
            idx = ord(character) - ord("a")
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        path = []
        for character in prefix:
            idx = ord(character) - ord("a")
            if not curr.children[idx]:
                return prefix
            curr = curr.children[idx]
            path.append(character)
            if curr.is_end:
                return "".join(path)

        return prefix


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        words = sentence.split(" ")
        res = []
        for word in words:
            res.append(trie.startsWith(word))
        return " ".join(res)
