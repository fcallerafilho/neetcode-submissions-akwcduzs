class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(left, right, currArray):
            if left >= len(s):
                res.append(currArray[:])
                return None

            if right >= len(s):
                return
            
            if self.isPalindrome(s[left:right+1]):
                currArray.append(s[left:right+1])
                backtrack(right + 1, right + 1, currArray)
                currArray.pop()
            
            backtrack(left, right+1, currArray)

        backtrack(0, 0, [])
        return res


    def isPalindrome(self, s: str) -> bool:
        if not s: return False
        l = (len(s)-1) // 2
        r = len(s) // 2 

        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                return False
            l -= 1
            r += 1

        return True
