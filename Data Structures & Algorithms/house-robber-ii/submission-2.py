class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[:-1]
        nums2 = nums[1:]

        def dfs(i, nums, cache):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = max(nums[i] + dfs(i+2, nums, cache), dfs(i+1, nums, cache))
            return cache[i]

        return max(dfs(0, nums1, {}), dfs(0, nums2, {}))