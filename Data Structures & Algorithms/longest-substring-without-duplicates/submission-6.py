class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seq = set()
        l, r = 0, 0
        maxLen = 0

        while r < len(s):
            while s[r] in seq:
                seq.remove(s[l])
                l += 1

            seq.add(s[r])
            maxLen = max(maxLen, len(seq))
            r += 1

        return maxLen