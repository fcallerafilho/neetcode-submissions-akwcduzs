class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        
        for k in range(0, len(sorted_nums)):
            if k > 0 and sorted_nums[k] == sorted_nums[k-1]:
                continue

            i = k + 1
            j = len(sorted_nums) - 1

            while i < j:
                if sorted_nums[i] + sorted_nums[j] < -sorted_nums[k]:
                    i += 1
                elif sorted_nums[i] + sorted_nums[j] > -sorted_nums[k]:
                    j -= 1
                elif sorted_nums[i] + sorted_nums[j] == -sorted_nums[k]:
                    res.append([sorted_nums[k], sorted_nums[i], sorted_nums[j]])
                    i += 1
                    j -= 1
                    
                    while i < j and sorted_nums[i] == sorted_nums[i-1]:
                        i += 1

        return res