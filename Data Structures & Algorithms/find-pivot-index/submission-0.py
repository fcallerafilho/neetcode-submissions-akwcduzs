class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for n in nums:
            total += n
            prefix.append(total)
        
        postfix = []
        total = 0
        for n in reversed(nums):
            total += n
            postfix.append(total)

        postfix.reverse()

        pivot = 0

        while pivot < len(nums):
            if prefix[pivot] == postfix[pivot]:
                return pivot
            pivot += 1

        return -1
