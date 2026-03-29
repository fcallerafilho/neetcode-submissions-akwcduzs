class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, currArray):
            if sum(currArray) == target:
                res.append(currArray[:])
                return
            
            if sum(currArray) > target or i >= len(nums):
                return

            currArray.append(nums[i])
            backtrack(i, currArray)

            currArray.pop()
            backtrack(i+1, currArray)
        
        backtrack(0, [])
        return res