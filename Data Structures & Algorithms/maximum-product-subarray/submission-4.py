class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currProd = 1
        maxProd = float('-inf')
        
        for n in nums:
            currProd = currProd * n
            maxProd = max(maxProd, currProd, n) 
            if n == 0:
                currProd = 1

        currProd = 1
        for n in reversed(nums):
            currProd = currProd * n
            maxProd = max(maxProd, currProd, n)
            if n == 0:
                currProd = 1

        return maxProd