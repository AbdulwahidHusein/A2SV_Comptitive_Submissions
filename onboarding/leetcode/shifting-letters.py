class Solution:
    def shift(self, w, dist):
        return chr(ord('a') + (ord(w) + dist - ord('a'))%26)
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        ps = [0] * n
        for i in range(n-1, -1, -1):
            ps[i] += shifts[i]
            if i < n-1:ps[i] += ps[i+1]
        sl = [w for w in s]
        for i in range(n): 
            sl[i] = self.shift(sl[i], ps[i])
        return "".join(sl)
