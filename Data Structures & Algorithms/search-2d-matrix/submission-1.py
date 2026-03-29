class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break

        if l > r:
            return False

        L, R = 0, len(matrix[mid]) - 1

        while L <= R:
            midcol = (L + R) // 2
            if target > matrix[mid][midcol]:
                L = midcol + 1
            elif target < matrix[mid][midcol]:
                R = midcol - 1
            else:
                return True

        return False
        

        

                