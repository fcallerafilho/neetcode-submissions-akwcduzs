class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = 1
        minProd = 1
        res = float('-inf')
        
        for n in nums:
            curMax = maxProd
            maxProd = max(curMax*n, minProd*n, n) 
            minProd = min(curMax*n, minProd*n, n) 
            res = max(res, maxProd, minProd)

        return res