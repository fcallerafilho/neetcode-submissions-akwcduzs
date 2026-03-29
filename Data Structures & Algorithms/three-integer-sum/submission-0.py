class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        for L in range(len(nums)):
            for M in range(L+1, len(nums)):
                for R in range(M+1, len(nums)):
                    if nums[L] + nums[M] + nums[R] == 0:
                        ans.add(tuple([nums[L], nums[M], nums[R]]))

        return [list(i) for i in ans]






        