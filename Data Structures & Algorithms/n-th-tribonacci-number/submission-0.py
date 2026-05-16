class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}

        # returns nth tribonacci number
        def dfs(n):
            if n <= 0:
                return 0
            if n <= 2:
                return 1
            if n in cache:
                return cache[n]

            res = dfs(n-1) + dfs(n-2) + dfs(n-3)

            cache[n] = res
            return res
            
        return dfs(n)