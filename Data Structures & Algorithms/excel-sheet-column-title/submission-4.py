class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        self.res = ''
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chars = [c for c in alphabet]
        nums = [i for i in range(1,27)]
        nums_to_chars = dict(zip(nums, chars))


        def divideNumber(colNum: int) -> str:
            if colNum <= 26:
                return nums_to_chars[colNum]

            self.res += divideNumber(colNum // 26)
            self.res += divideNumber(colNum % 26)

            return self.res

        return divideNumber(columnNumber)