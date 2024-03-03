class Solution:
    def is_possible(self, board, row, col, num):
        s = len(board)
        for i in range(s):
            if board[i][col] == num or board[row][i] == num:
                return False
        rg = row - row % 3
        cg = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[rg + i][cg + j] == num:
                    return False
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in range(1, 10):
                            if self.is_possible(board, i, j, str(num)):
                                board[i][j] = str(num)
                                if solve():
                                    return True
                                board[i][j] = "."
                        return False
            return True
        
        solve()