class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeating = {}
        l, r = 0, 0
        maxLen = 0

        while r < len(s):
            if s[r] in repeating:
                l = repeating[s[r]][0] + 1
                r = l
                repeating = {}
            repeating[s[r]] = (r, 1)
            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen