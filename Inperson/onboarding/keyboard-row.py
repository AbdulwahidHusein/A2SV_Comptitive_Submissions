class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            "qwertyuiop",  "asdfghjkl", "zxcvbnm"
        ]
        def is_in_row(i, word):
            for w in word.lower():
                if not w in rows[i]:
                    return False
            return True
        ans = []
        for word in words:
            if is_in_row(0, word) or is_in_row(1, word) or is_in_row(2, word):
                ans.append(word)
        return ans