class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [1, 1]
        i = 2

        while i <= n:
            aux = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = aux
            i += 1

        return dp[1]
