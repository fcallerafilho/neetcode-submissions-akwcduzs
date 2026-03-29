class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currSet, subsets = [], []

        def backtracker(i):
            if i >= len(nums):
                subsets.append(currSet[:])
                return None
            
            currSet.append(nums[i])
            backtracker(i+1)

            currSet.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtracker(i+1)

        backtracker(0)
        return subsets

