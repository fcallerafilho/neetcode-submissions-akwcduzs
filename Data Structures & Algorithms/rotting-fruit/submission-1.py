class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(row, col, time):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if grid[row][col] == 0 or (grid[row][col] > 1 and grid[row][col] < time):
                return
            
            grid[row][col] = time
            dfs(row + 1, col, time + 1)
            dfs(row - 1, col, time + 1)
            dfs(row, col - 1, time + 1)
            dfs(row, col + 1, time + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    dfs(r, c, 2)

        total_time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
                if grid[r][c] >= 2:
                    total_time = max(total_time, grid[r][c] - 2)

        return total_time