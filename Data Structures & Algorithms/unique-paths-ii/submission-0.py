class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n_rows, n_cols = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(r, c, cache):
            if r == n_rows or c == n_cols or obstacleGrid[r][c] == 1:
                return 0
            if r == n_rows-1 and c == n_cols-1:
                return 1
            if (r, c) in cache:
                return cache[(r, c)]

            cache[(r,c)] = dfs(r+1, c, cache) + dfs(r, c+1, cache)
            return cache[(r, c)]

        return dfs(0, 0, {})
            