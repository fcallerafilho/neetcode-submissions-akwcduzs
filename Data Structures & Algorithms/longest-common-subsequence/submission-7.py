class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        cols = len(text1) + 1
        rows = len(text2) + 1

        prevRow = [0] * cols

        for r in range(rows - 2, -1, -1):
            currRow = [0] * cols
            for c in range(cols - 2, -1, -1):
                if text2[r] == text1[c]:
                    currRow[c] = 1 + prevRow[c + 1]
                else:
                    currRow[c] = max(prevRow[c], currRow[c + 1])
            prevRow = currRow

        return currRow[0]
