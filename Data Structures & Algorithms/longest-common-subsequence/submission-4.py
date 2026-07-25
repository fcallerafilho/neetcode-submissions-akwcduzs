class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)
        
        for i in range(len(text1)):
            currRow = [0] * (len(text2) + 1)
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    currRow[j+1] = 1 + dp[j]
                else:
                    currRow[j+1] = max(dp[j+1], currRow[j])
            dp = currRow
                
        return currRow[-1]