class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(col):
            if col == n:
                res.append(["".join(row) for row in board])
                return
            
            for row in range(n):
                if self.allowed(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(col + 1)
                    board[row][col] = '.'

        backtrack(0)
        return res
            
    def allowed(self, board, row, col):
        n = len(board)

        for j in range(col):
            if board[row][j] == 'Q':
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = row + 1, col - 1
        while i < n and j >= 0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1

        return True
