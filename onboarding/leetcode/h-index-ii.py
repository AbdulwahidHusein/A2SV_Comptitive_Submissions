class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2
            if n - mid > citations[mid]:
                left = mid + 1
            elif n-mid < citations[mid]:
                right = mid - 1
            else:
                return n - mid
        return n - left