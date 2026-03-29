class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(currString, opening, closing):
            if opening > n:
                return
            if closing > opening:
                return
            if opening == n and closing == n:
                res.append(currString)
                return

            backtrack(currString + '(', opening + 1, closing)
            backtrack(currString + ')', opening, closing + 1)

        backtrack("", 0, 0)
        return res



