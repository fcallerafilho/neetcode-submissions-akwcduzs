class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, path, currSum):
            if currSum == target:
                res.append(path[:])
                return

            for j in range(i, len(nums)):
                if currSum > target:
                    return
                path.append(nums[j])
                backtrack(j, path, currSum + nums[j])
                path.pop()

        
        backtrack(0, [], 0)
        return res