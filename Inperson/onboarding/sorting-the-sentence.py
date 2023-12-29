class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        n = len(words)
        ans = [""]*n
        for word in words:
            pos = int(word[-1])
            ans[pos-1] = word[:-1]
        return " ".join(ans)