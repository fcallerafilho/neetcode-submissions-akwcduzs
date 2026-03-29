class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in mySet:
                length = 0
                while (nums[i] + length) in mySet:
                    length += 1
                longest = max(length, longest)

        return longest