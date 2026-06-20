class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        # returns LIS
        def dfs(i, prev):
            if (i, prev) in cache:
                return cache[(i, prev)]
            if i == len(nums):
                return 0

            lis = dfs(i + 1, prev)

            if prev == -1 or nums[i] > nums[prev]:
                lis = max(lis, 1 + dfs(i + 1, i))

            cache[(i, prev)] = lis
            return lis

        return dfs(0, -1)
