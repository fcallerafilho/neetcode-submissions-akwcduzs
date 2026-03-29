class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(row, col):
            if min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0
            if grid[row][col] == '0':
                return 0

            grid[row][col] = '0'

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

            return 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                count += dfs(row, col)

        return count

        
            