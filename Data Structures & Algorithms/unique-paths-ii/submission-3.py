class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        prevRow = [0] * len(obstacleGrid[0])

        for r in range(len(obstacleGrid) - 1, -1, -1):
            currRow = obstacleGrid[r]

            for c in range(len(obstacleGrid[0]) - 1, -1, -1):
                if currRow[c] == 1:
                    currRow[c] = 0
                elif r == len(obstacleGrid) - 1 and c == len(obstacleGrid[0]) - 1:
                    currRow[c] = 1
                else:
                    currRow[c] = prevRow[c] 
                    if c < len(obstacleGrid[0]) - 1:
                        currRow[c] += currRow[c+1]

            prevRow = currRow

        return prevRow[0]