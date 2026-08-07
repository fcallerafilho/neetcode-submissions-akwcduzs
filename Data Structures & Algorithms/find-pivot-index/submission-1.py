class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            total += n

        lsum = 0
        for i in range(len(nums)):
            rsum = total - nums[i] - lsum
            if lsum == rsum:
                return i
            lsum += nums[i]

        return -1            
            