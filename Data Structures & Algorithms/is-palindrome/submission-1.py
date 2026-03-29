class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = ''

        for i in range(len(s)):
            if s[i].isalnum():
                s_alnum += s[i]
            else:
                s_alnum += ''

        s_alnum = s_alnum.lower()

        # print(s_alnum)

        L, R = 0, len(s_alnum) - 1  

        while (R > L):
            if s_alnum[L] == s_alnum[R]:
                R -= 1
                L += 1
            else:
                return False
        
        return True

       