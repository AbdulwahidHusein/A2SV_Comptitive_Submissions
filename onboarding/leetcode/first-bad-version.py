# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left  = 1
        mid = n//2
        right = n
        while left <= right:
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2
        return mid + 1