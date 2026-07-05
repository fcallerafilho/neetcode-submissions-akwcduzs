class Solution:
    def climbStairs(self, n: int) -> int:
        self.ways = 0
        memo = {}

        def dfs(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            

            self.ways = dfs(n-1)
            self.ways += dfs(n-2)

            memo[n] = self.ways
            return memo[n]

        return dfs(n)