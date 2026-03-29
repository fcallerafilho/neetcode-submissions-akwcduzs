class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        for char in set(s):
            l, r = 0, 0
            temp_k = k
            while r < len(s):
                if s[r] == char:
                    r += 1
                elif temp_k > 0:
                    temp_k -= 1
                    r += 1
                else:
                    if s[l] != char:
                        temp_k += 1
                    l += 1
                maxlen = max(maxlen, r - l)
        return maxlen