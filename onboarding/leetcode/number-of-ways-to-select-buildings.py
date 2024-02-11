class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        left_zeros = [0]*n
        right_zeros = [0]*n

        for i in range(1, n):
            if s[i-1] == '0':
                left_zeros[i] += left_zeros[i-1] + 1
            else:
                left_zeros[i] += left_zeros[i-1]
        for i in range(n-2, -1, -1):
            if s[i+1] == '0':
                right_zeros[i] += right_zeros[i+1] + 1
            else:
                right_zeros[i] += right_zeros[i+1]
        ans = 0
        for i in range(n):
            if s[i] == '1':
                ans += left_zeros[i] * right_zeros[i]
            else:
                ans += (i - left_zeros[i]) * (n - i - right_zeros[i] -1)
        return ans