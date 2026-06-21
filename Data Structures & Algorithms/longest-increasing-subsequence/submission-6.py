class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(i):
            if memo[i] != -1:
                return memo[i]
            lis = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    lis = max(lis, 1 + dfs(j))

            memo[i] = lis
            return lis

        return max(dfs(i) for i in range(len(nums)))