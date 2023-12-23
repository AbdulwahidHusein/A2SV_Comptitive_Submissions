class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        original = words.copy()
        alien_index = {}
        for i in range(26):
            alien_index[order[i]] = i
        words.sort(key = lambda word : [alien_index[w] for w in word])
        return original == words