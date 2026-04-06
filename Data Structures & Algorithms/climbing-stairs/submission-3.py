class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(n, cache):
            if n == 0:
                return 1
            if n in cache:
                return cache[n]
            if n < 0:
                return 0
            
            cache[n] = dfs(n-1, cache) + dfs(n-2, cache)
            return cache[n]

        return dfs(n, {})