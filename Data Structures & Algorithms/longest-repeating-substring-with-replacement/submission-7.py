class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freqs = {}
        res = 0

        while r < len(s):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            
            # if length of current string - most frequent character > k, keep popping at the left
            while freqs and (r - l + 1) - max(freqs.values()) > k:
                freqs[s[l]] = freqs.get(s[l]) - 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res