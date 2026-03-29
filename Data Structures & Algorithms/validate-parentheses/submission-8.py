class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"(", "[", "{"}
        closing = {")", "]", "}"}
        if len(s) <= 1 or s[0] in closing:
            return False
        arr = []

        for i in range(len(s)):
            if s[i] in opening:
                arr.append(s[i])
            elif s[i] in closing and len(arr) != 0:
                pair = arr.pop()
                if s[i] == ')' and pair == '(':
                    continue
                elif s[i] == ']' and pair == '[':
                    continue
                elif s[i] == '}' and pair == '{':
                    continue
                else:
                    return False
            else:
                return False
        
        return True if len(arr) == 0 else False
        


    
    