class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n%3 >1:
                return False
            n = n//3
        return True