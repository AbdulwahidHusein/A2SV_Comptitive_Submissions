# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        MAX = int(c**0.5)
        smaller = 0
        larger = MAX
        while smaller <= larger:
            product = smaller*smaller + larger*larger
            if product == c:
                return True
            elif product > c:
                larger -= 1
            else:
                smaller += 1
        return False