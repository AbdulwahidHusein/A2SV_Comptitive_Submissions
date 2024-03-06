class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = (m*n-1)
        
        while left <= right:
            mid = (left+right) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                return True
        return False



