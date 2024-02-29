class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        n = len(word)
        def search(row, col, idx):
            if idx == n:
                return True
            if row < 0 or col < 0 or row == rows or col == cols:
                return False
            if board[row][col] != word[idx]:
                return False
            c = board[row][col]
            board[row][col] = " "
            if search(row+1, col, idx+1) or search(row-1, col, idx+1) or search(row, col+1, idx+1) or search(row, col-1, idx+1):
                return True
            else:
                board[row][col] = c
                return False
        for i in range(rows):
            for j in range(cols):
                if search(i, j, 0):
                    return True
        return False
                    