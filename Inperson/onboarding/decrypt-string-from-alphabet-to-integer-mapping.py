class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        n = len(s)
        i = 0
        while i < n-2:
            if s[i+2] == "#":
                ans.append(chr(ord('a') -1 + int(s[i:i+2])))
                i+= 3
            else:
                ans.append(chr(ord('a')-1 + int(s[i])))
                i += 1
        while i < n:
            ans.append(chr(ord('a')-1 + int(s[i])))
            i += 1
        return "".join(ans)