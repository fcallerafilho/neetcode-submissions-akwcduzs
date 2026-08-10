class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProds = []
        suffixProds = []
        total = 1

        for n in nums:
            total *= n
            prefixProds.append(total)

        total = 1
        for n in reversed(nums):
            total *= n
            suffixProds.append(total)

        suffixProds.reverse()
        suffixProds.append(1)
        res = []

        for i in range(len(nums)):
            except_self = prefixProds[i-1] * suffixProds[i+1] if i > 0 else suffixProds[i+1]
            res.append(except_self)

        return res

