class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(r, c, cache):
            if r == m-1 and c == n-1:
                return 1
            if r >= m or c >= n:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]

            n_ways = dfs(r+1, c, cache) + dfs(r, c+1, cache)

            cache[r][c] = n_ways
            return cache[r][c]

        return dfs(0, 0, [[0]*n for i in range(m)])