class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(i):
            if i == len(nums):
                return 0
            if i in memo:
                return memo[i]

            lis = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    lis = max(lis, 1 + dfs(j))

            memo[i] = lis
            return lis
        
        return max(dfs(i) for i in range(len(nums)))