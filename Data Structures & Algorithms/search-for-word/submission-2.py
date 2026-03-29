class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        i = 0
        visited = {}

        def backtrack(row, col, i):
            if i == len(word):
                return True
            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
                return False
            if board[row][col] != word[i]:
                return False
            if (row, col) in visited:
                return False
            if board[row][col] == word[i]:
                visited[(row, col)] = 1
                up = backtrack(row-1, col, i+1)
                down = backtrack(row+1, col, i+1)
                left = backtrack(row, col-1, i+1)
                right = backtrack(row, col+1, i+1)

                del visited[(row, col)]
            else:
                return False

            return up or down or left or right
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[i]:
                    if backtrack(row, col, i):
                        return True

        return False

        
            





