class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i):
            if i == len(nums):
                return [[]]
            
            resPerms = []
            permutations = backtrack(i+1)

            for permutation in permutations:
                for index in range(len(permutation) + 1):
                    permutation_copy = permutation.copy()
                    permutation_copy.insert(index, nums[i])
                    resPerms.append(permutation_copy)
            
            return resPerms
        
        return backtrack(0)
