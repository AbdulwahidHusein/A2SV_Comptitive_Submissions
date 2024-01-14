class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcounter = Counter(t)      
        left = 0
        right = 0
        count = Counter()
        n = len(s)
        leng = 10**5
        substr = ""

        for i in range(n):
            count[s[i]] += 1
            while tcounter - count == Counter():
                if leng >  i - left + 1:
                    substr = s[left:i+1]
                    leng = i - left + 1
                count[s[left]] -= 1
                left += 1
                
        return substr
