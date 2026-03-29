class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, currArray):
            if sum(currArray) == target:
                res.append(currArray[:])
                return
            if sum(currArray) > target or i >= len(candidates):
                return

            currArray.append(candidates[i])
            backtrack(i+1, currArray)

            currArray.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, currArray)

        backtrack(0, [])
        return res

        