class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.visited = set()
        def dfs(row, col, dist):
            if min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]):
                return 
            if grid[row][col] == -1:
                return 
            if (row, col) in self.visited:
                return
            if dist > grid[row][col]:
                return
            
            self.visited.add((row, col))

            dfs(row + 1, col, dist+1)
            dfs(row - 1, col, dist+1)
            dfs(row, col - 1, dist+1)
            dfs(row, col + 1, dist+1)

            self.visited.remove((row, col))

            grid[row][col] = dist

            return

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    dfs(row, col, 0)
        




            
