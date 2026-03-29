class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1

        while l <= r:
            midrow = (l + r) // 2
            L, R = 0, len(matrix[midrow]) - 1

            while L <= R:
                midcol = (L + R) // 2

                if target > matrix[midrow][midcol]:
                    L = midcol + 1
                elif target < matrix[midrow][midcol]:
                    R = midcol - 1
                else:
                    return True

            if target > matrix[midrow][-1]:
                l = midrow + 1
            else:
                r = midrow - 1

        return False
