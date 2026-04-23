class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        l_res, r_res = 0, 0

        for i in range(len(s)):
            if self.helper(s, i, i)[0] > length:
                length, l_res, r_res = self.helper(s, i, i)

            if self.helper(s, i, i+1)[0] > length:
                length, l_res, r_res = self.helper(s, i, i+1)
            
        return s[l_res : r_res]

    def helper(self, s, l, r) -> tuple:
        maxLen = 0      
        l_i, r_i = 0, 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > maxLen:
                maxLen = (r - l + 1)
                l_i = l
                r_i = r + 1
            l -= 1
            r += 1
        
        return (maxLen, l_i, r_i)

        
