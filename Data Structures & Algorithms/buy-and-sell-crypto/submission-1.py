class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0

        for R in range(len(prices)):
            print(L, R)
            if prices[L] > prices[R]:
                L = R
            elif prices[R] > prices[L]:
                profit = max(profit, prices[R] - prices[L])
            
        return profit
