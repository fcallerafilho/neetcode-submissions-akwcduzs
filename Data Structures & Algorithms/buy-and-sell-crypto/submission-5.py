class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 0

        while r < len(prices) - 1:
            if prices[l] > prices[r]:
                l = r
            while r < len(prices) - 1 and prices[r] <= prices[r+1]:
                r += 1
            profit = max(profit, prices[r] - prices[l])
            r += 1
            
        return profit
            
            

        

        
