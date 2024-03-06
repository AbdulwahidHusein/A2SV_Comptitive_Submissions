class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 1
        right = x//2
        while left <= right:
            mid = (left+right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        return left - 1