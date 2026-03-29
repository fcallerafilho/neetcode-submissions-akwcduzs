class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        visited = set()

        def dfs(row, col):
            if min(row, col) < 0 or row >= len(image) or col >= len(image[0]):
                return
            if image[row][col] != original:
                return
            if (row, col) in visited:
                return

            visited.add((row, col))
            image[row][col] = color
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

            return

        dfs(sr, sc)
        return image