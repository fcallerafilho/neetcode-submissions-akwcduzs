class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}

        for i in range(len(nums)):
            if nums[i] in myMap:
                return True
            elif nums[i] not in myMap:
                myMap[nums[i]] = 1
            
        return False