class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return n%4 == 0 and self.isPowerOfFour(n//4)