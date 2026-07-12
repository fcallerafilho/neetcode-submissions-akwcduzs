class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
            
        q = collections.deque()
        q.append((0, 0))
        visited = set()
        length = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        while len(q) > 0:
            length += 1
            for i in range(len(q)):
                r, c = q.popleft()
                visited.add((r, c))

                if r == len(grid)-1 and c == len(grid[0])-1:
                    return length

                for dr, dc in directions:
                    if min(r + dr, c + dc) < 0 or r + dr == len(grid) or c + dc == len(grid[0]) or grid[r+dr][c+dc] == 1 or (r + dr, c + dc) in visited:
                        continue
                    else:
                        q.append((r+dr, c+dc))

            
        return -1