class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = [] 
        k = len(digits)
        map_ = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(i, currStr):
            if len(currStr) == k:
                combinations.append(currStr)
                return None
            
            for char in map_[digits[i]]:
                backtrack(i + 1, currStr + char)
        
        if digits:
            backtrack(0, '')

        return combinations
