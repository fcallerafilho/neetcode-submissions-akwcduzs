class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSet, subset = [], []

        def helper(i, nums, currSet, subset):
            if i >= len(nums):
                subset.append(currSet.copy())
                return None

            currSet.append(nums[i])
            helper(i + 1, nums, currSet, subset)

            currSet.pop()
            helper(i + 1, nums, currSet, subset)

        helper(0, nums, currSet, subset)
        return subset


    