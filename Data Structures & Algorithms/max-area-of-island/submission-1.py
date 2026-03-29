class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.visited = set()
        count = float('-inf')

        def dfs(row, col, cnt):
            if min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0
            elif grid[row][col] == 0:
                return 0
            elif (row, col) in self.visited:
                return 0

            self.visited.add((row, col))

            up = dfs(row+1, col, cnt)
            down = dfs(row-1, col, cnt)
            left = dfs(row, col-1, cnt)
            right = dfs(row, col+1, cnt)

            return 1+up+down+left+right

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                count = max(count, dfs(row, col, 0))

        return count

        
            
