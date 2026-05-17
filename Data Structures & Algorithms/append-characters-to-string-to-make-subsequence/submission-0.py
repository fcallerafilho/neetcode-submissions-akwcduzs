class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # t needs to become subsequence of s
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                j += 1
            i += 1

        if j == len(t):
            return 0
        else:
            return len(t) - j
             