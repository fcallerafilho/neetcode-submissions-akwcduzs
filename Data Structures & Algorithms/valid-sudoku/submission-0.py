class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            visited = set()
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                elif board[r][c] not in visited:
                    visited.add(board[r][c])
                else:
                    return False
        
        for c in range(len(board[0])):
            visited = set()
            for r in range(len(board)):
                if board[r][c] == '.':
                    continue
                elif board[r][c] not in visited:
                    visited.add(board[r][c])
                else:
                    return False

        r_start, r_end = 0, 3
        c_start, c_end = 0, 3
        for i in range(0, 3):
            for j in range(0, 3):
                visited = set()
                for r in range(r_start, r_end):
                    if r >= len(board):
                        break
                    for c in range(c_start, c_end):
                        if c >= len(board[0]):
                            break
                        if board[r][c] == '.':
                            continue
                        elif board[r][c] not in visited:
                            visited.add(board[r][c])
                        else:
                            return False
                
                c_start += 3
                c_end += 3

            r_start += 3
            r_end += 3
        
        return True


            

        
