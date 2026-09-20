class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        l = 0
        maxLen = 0

        for r in range(len(s)):
            if s[r] in chars:
                l = max(l, chars[s[r]] + 1)
            
            chars[s[r]] = r
            maxLen = max(maxLen, r - l + 1)

        return maxLen
