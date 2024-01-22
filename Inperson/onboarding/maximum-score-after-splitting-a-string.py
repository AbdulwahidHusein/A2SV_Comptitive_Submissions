class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        left_zeros = [0]*(n)
        left_zeros[0] = int(not int(s[0]))

        for i in range(1, n):
            left_zeros[i] = left_zeros[i-1] + int(not int(s[i]))
  
        ans = 0
        ones = 0
        for j in range(n-1, 0, -1):
            if s[j] == '1':
                ones += 1
            ans = max(ans, ones + left_zeros[j-1])
            
        return ans

        #0 1 2 3 4