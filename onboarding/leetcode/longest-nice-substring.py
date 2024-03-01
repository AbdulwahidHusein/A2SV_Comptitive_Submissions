class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def pos(count):
            for a in count:
                if count[a.lower()] < 1 or count[a.upper()] < 1:
                    return False
            return True
        n = len(s)
        nice = [0, 0]
        for j in range(n):
            for i in range(j):
                c = Counter(s[i:j+1])
                if pos(c):
                    if j - i + 1 > nice[1] - nice[0]:
                        nice = [i, j+1]
        return s[nice[0]: nice[1]]