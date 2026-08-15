class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = 0
        chars = {}

        while r < len(s):
            if s[r] in chars:
                l = max(chars[s[r]] + 1, l)

            chars[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen