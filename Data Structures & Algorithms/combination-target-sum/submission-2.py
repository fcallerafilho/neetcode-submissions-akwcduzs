class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, currArray):
            if sum(currArray) == target:
                res.append(currArray[:])
                return

            for j in range(i, len(nums)):
                if sum(currArray) > target:
                    return
                currArray.append(nums[j])
                backtrack(j, currArray)
                currArray.pop()

        
        backtrack(0, [])
        return res