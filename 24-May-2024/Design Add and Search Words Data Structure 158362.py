# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

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

    def search(self, prefix: str, root) -> bool:
        if not root:
            return False
        curr = root
        for i, character in enumerate(prefix):
            if character != ".":
                idx = ord(character) - ord("a")
                if not curr.children[idx]: 
                    return False
                curr = curr.children[idx]
            else:
                if i == len(prefix) -1 and any(curr.children):
                    for i in range(26):
                        if curr.children[i] and curr.children[i].is_end:
                            return True
                pref = prefix[i+1:]
                for j in range(26):
                    if self.search(pref, curr.children[j]):
                        return True
                return False
        return curr.is_end 


            

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)
 
    def search(self, word: str) -> bool:
        return self.trie.search(word, self.trie.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)