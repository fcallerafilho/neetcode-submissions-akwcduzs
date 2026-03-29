class Solution:
    def validPalindrome(self, s: str) -> bool:
        i , j = 0, len(s) - 1
        deleted = False

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif deleted:
                return False
            elif s[i+1] == s[j] and self.palindrome(s[0:i] + s[i+1:len(s)]):
                deleted = True
                i += 1
            elif s[i] == s[j-1] and self.palindrome(s[0:j] + s[j+1:len(s)]):
                deleted = True
                j -= 1
            else:
                return False

        return True
        
    def palindrome(self, s: str) -> bool:
        print(s)
        i , j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True