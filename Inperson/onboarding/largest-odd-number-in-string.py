class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        while n > 0:
            if int(num[n-1])%2 == 0:
                n -= 1
            else:
                break
        return num[:n]
        