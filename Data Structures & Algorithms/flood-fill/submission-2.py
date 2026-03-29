class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]

        def dfs(row, col):
            if min(row, col) < 0 or row >= len(image) or col >= len(image[0]):
                return
            if image[row][col] != original:
                return
            if visited[row][col] == True:
                return

            visited[row][col] = True
            image[row][col] = color
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

            return

        dfs(sr, sc)
        return image