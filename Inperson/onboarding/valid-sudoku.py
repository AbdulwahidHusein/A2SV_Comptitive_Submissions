class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #lets brutforce
        def is_row_valid(i):
            c = Counter(board[i])
            for n in c:
                if c[n] > 1 and n != ".":
                    return False
            return True
        def is_col_valid(j):
            c = defaultdict(int)
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in c:
                        return False
                    c[board[i][j]] += 1
            return True
        def is_33_valid():
            for i in range(0,9,3):
                for j in range(0,9,3):
                    c = defaultdict(int)
                    for x in range(3):
                        for y in range(3):
                            if board[i+x][j+y] != ".":
                                if board[i+x][j+y] in c:
                                    return False
                                c[board[i+x][j+y]]  += 1
            return True
        is_col = True 
        is_row = True
        for i in range(9):
            is_col = is_col and is_col_valid(i)
        for i in range(9):
            is_row = is_row and is_row_valid(i)
       
        return is_33_valid() and is_col and is_row
