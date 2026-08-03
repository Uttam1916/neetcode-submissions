class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, index):
            if index == len(word):
                return True

            temp = board[i][j]
            board[i][j] = "#"

            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for d in directions:
                r = i + d[0]
                c = j + d[1]

                if (
                    0 <= r < len(board) and
                    0 <= c < len(board[0]) and
                    board[r][c] == word[index]
                ):
                    if dfs(r, c, index + 1):
                        board[i][j] = temp
                        return True

            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True

        return False