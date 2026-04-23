class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_i, r_i = 0, 0
        maxLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = (r - l + 1)
                    l_i = l
                    r_i = r + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = (r - l + 1)
                    l_i = l
                    r_i = r + 1
                l -= 1
                r += 1

        return s[l_i : r_i]
