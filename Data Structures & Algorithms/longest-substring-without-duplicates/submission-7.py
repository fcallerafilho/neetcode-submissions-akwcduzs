class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = 0
        chars = {}

        while r < len(s):
            while s[r] in chars:
                chars.pop(s[l])
                l += 1

            maxLen = max(maxLen, r - l + 1)
            chars[s[r]] = chars.get(s[r], 0) + 1
            r += 1

        return maxLen