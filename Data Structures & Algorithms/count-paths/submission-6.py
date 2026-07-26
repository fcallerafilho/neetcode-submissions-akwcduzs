class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n

        for r in range(m-1, -1, -1):
            currRow = [0] * n
            currRow[-1] = 1
            for c in range(len(currRow)-2, -1, -1):
                currRow[c] += prevRow[c] + currRow[c+1]
            prevRow = currRow

        return currRow[0]
