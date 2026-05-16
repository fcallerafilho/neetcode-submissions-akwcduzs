class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(rem):
            if rem in cache:
                return cache[rem]
            if rem == 0:
                return 0

            res = 1e9
            for coin in coins:
                if rem - coin >= 0:
                    res = min(res, 1 + dfs(rem - coin))

            cache[rem] = res
            return res

        return -1 if dfs(amount) >= 1e9 else dfs(amount)
            