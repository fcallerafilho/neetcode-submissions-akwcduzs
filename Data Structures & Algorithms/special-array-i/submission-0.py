class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l, r = 0, 1

        while r <= len(nums)-1:
            if (nums[l] % 2 == 0 and nums[r] % 2 != 0) or (nums[l] % 2 != 0 and nums[r] % 2 == 0):
                l += 1
                r += 1
            else:
                return False
            
        return True