from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperBound = max(piles)
        rates = range(1, upperBound+1)
        l, r = 0, len(rates) - 1
        k = float('inf')
        
        while l <= r:
            mid = (l+r) // 2
            hours = 0

            for j in range(len(piles)):
                hours += ceil(piles[j]/rates[mid])

            if hours > h:
                l = mid + 1
            elif hours <= h:
                r = mid - 1
                k = min(k, rates[mid])

        return k