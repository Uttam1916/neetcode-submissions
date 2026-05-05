class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] != ".":
                            if board[k][l] in grid:
                                return False
                            grid.add(board[k][l])

        return True