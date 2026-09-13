class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSeq = 0

        for n in nums:
            if n - 1 not in numSet:
                currSeq = 1
                i = n + 1
                while i in numSet:
                    currSeq += 1
                    i += 1

                maxSeq = max(maxSeq, currSeq)

        return maxSeq 