class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i, cache):
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]

            left = dfs(i+1, cache)
            right = dfs(i+2, cache)

            cache[i] = cost[i] + min(left, right)
            return cache[i]

        return min(dfs(0, {}), dfs(1, {}))