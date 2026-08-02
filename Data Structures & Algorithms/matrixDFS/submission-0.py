class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        path = set()
        def dfs(r, c):
            if r == len(grid) or c == len(grid[0]) or min(r, c) < 0 or grid[r][c] == 1:
                return 0
            if (r, c) in path:
                return 0
            if r == len(grid)-1 and c == len(grid[0]) - 1:
                return 1

            path.add((r, c))
            up = dfs(r+1, c)
            down = dfs(r-1, c)
            left = dfs(r, c-1)
            right = dfs(r, c+1)
            path.remove((r, c))

            return up + down + left + right

        return dfs(0, 0)


            