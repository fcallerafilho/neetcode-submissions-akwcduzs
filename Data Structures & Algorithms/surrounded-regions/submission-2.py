class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        def dfs(row, col, surrounded):
            if (row, col) in visited:
                return set()
            if board[row][col] == 'X':
                return set()
            if board[row][col] == "O" and (row == 0 or row == len(board)-1 or col == 0 or col == len(board[0])-1):
                return {None}
            
            visited.add((row, col))
            surrounded.add((row, col))

            surrounded.update(dfs(row+1, col, surrounded))
            surrounded.update(dfs(row-1, col, surrounded))
            surrounded.update(dfs(row, col+1, surrounded))
            surrounded.update(dfs(row, col-1, surrounded))

            visited.remove((row, col))

            return surrounded


        for row in range(len(board)):
            for col in range(len(board[0])):
                s = set()
                dfs(row, col, s)

                if len(s) > 0 and None not in s:
                    for r, c in s:
                        board[r][c] = 'X'

        
                


            


