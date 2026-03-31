class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        
        mid = (l+r) // 2
        if target > nums[mid]:
            return mid + 1
        elif target < nums[mid]:
            return mid - 1 if mid > 0 else 0
        