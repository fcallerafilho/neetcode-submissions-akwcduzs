class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        currRow = [0] * n
        currRow[-1] = 1

        for r in range(m-1, -1, -1):
            prevRow = [0] * n
            for c in range(len(currRow)-1, -1, -1):
                currRow[c] += prevRow[c]
                if c+1 < n:
                    currRow[c] += currRow[c+1]
            prevRow = currRow

        return currRow[0]
