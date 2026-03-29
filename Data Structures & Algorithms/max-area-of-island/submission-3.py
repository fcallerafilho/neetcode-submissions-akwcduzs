class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = float('-inf')

        def dfs(row, col):
            if min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0
            elif grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            up = dfs(row+1, col)
            down = dfs(row-1, col)
            left = dfs(row, col-1)
            right = dfs(row, col+1)

            return 1 + up + down + left + right

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                count = max(count, dfs(row, col))

        return count

        
            
