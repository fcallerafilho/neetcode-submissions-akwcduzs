class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxlen = 0
        freqs = dict()
        maxfreq = 0

        while r < len(s):
            freqs[s[r]] = 1 + freqs.get(s[r], 0)
            maxfreq = max(maxfreq, freqs[s[r]])
            
            while (r - l + 1) - maxfreq > k:
                freqs[s[l]] -= 1
                l += 1

            maxlen = max(r - l + 1, maxlen)
            r += 1

        return maxlen
            
               
            
            
