class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freqs = {}
        maxLen = 0

        while r < len(s):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            while freqs and ((r - l + 1) - max(freqs.values())) > k:
                freqs[s[l]] = freqs.get(s[l], 0) - 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen