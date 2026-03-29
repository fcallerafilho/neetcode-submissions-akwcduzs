class Solution:
    n_ways = 0
    def climbStairs(self, n: int) -> int:
        if n == 0:
            self.n_ways += 1
            return 
        elif n < 0:
            return self.n_ways
        
        self.climbStairs(n-1)
        self.climbStairs(n-2)

        return self.n_ways