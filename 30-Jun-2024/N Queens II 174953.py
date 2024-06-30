# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def check_placement(self, board, row, col):
        def check_diagonal(row, col, board):
            n = len(board)
            i, j = row, col
            while i > 0 and j > 0:
                i -= 1
                j -= 1
                if board[i][j] == "Q":
                    return False
            
            i, j = row, col
            while i < n - 1 and j < n - 1:
                i += 1
                j += 1
                if board[i][j] == "Q":
                    return False
            i, j = row, col
            while i < n - 1 and j > 0:
                i += 1
                j -= 1
                if board[i][j] == "Q":
                    return False
            
            i, j = row, col
            while i > 0 and j < n - 1:
                i -= 1
                j += 1
                if board[i][j] == "Q":
                    return False 
            return True 
        n = len(board)
        for i in range(n):
            if  board[i][col] == "Q" or board[row][i] == "Q":
                return False
        return check_diagonal(row, col, board)

    def totalNQueens(self, n: int) -> int:         
        board = [["." for _ in range(n)] for _ in range(n)]
        ans = 0
        def solve(row):
            nonlocal board, ans
            if row == n:
                ans += 1
                return
            for col in range(n):
                if self.check_placement(board, row, col):
                    board[row][col] = "Q"
                    solve(row+1)
                    board[row][col] = "."
        
        solve(0)
        return ans