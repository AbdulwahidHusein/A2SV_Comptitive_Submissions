# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def canFill(x):
            count = 0
            prev = position[0]
            for i in range(1, len(position)):
                if position[i] - prev >= x:
                    count += 1
                    prev = position[i]
            return count >= m - 1
        small = 0
        large = position[-1]
        res = -1
        while small <= large:
            mid = (small + large) // 2
            if canFill(mid):
                small = mid + 1
                res = mid
            else:
                large = mid - 1
        return res
