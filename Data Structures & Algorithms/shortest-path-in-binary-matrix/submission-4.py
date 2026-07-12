class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # good clarifying question: top-left is at length 0 or 1?
        # if start is not 0, no paths available
        if grid[0][0] == 1:
            return -1

        q = collections.deque()
        q.append((0, 0))
        visited = set()
        length = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        while len(q) > 0:
            length += 1 # start at length 1
            for i in range(len(q)):
                r, c = q.popleft()

                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        min(nr, nc) < 0
                        or nr == len(grid)
                        or nc == len(grid[0])
                        or grid[nr][nc] == 1
                        or (nr, nc) in visited
                    ):
                        continue

                    q.append((nr, nc))
                    visited.add((nr, nc))

        # if end is marked with a 1, eventually all available nodes will be visited, emptying our queue, which will end up here
        return -1
