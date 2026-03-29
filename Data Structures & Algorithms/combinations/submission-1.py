class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        currComb, combinations = [], []

        def backtrack(i):
            if len(currComb) == k:
                combinations.append(currComb[:])
            if i > n:
                return None
            
            for j in range(i, n+1):
                currComb.append(j)
                backtrack(j+1)
                currComb.pop()

        backtrack(1)
        return combinations