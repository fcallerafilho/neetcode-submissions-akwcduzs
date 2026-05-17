class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        elif not t:
            return False
            
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                j += 1
            else:
                j += 1
                i += 1
                if i == len(s):
                    return True

        return False

        

            

