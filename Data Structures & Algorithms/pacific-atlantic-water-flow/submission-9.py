class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        res = []

        def dfs(row, col, prev, path):
            if min(row, col) < 0 or row == len(heights) or col == len(heights[0]) or heights[row][col] < prev or (row, col) in path:
                return

            path.add((row, col))

            dfs(row+1, col, heights[row][col], path)
            dfs(row-1, col, heights[row][col], path)
            dfs(row, col+1, heights[row][col], path)
            dfs(row, col-1, heights[row][col], path)

        for row in range(len(heights)):
            dfs(row, 0, float('-inf'), pacific)

        for col in range(len(heights[0])):
            dfs(0, col, float('-inf'), pacific)
        
        for row in range(len(heights)):
            dfs(row, len(heights[0]) - 1, float('-inf'), atlantic)

        for col in range(len(heights[0])):
            dfs(len(heights) - 1, col, float('-inf'), atlantic)

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])

        return res










            