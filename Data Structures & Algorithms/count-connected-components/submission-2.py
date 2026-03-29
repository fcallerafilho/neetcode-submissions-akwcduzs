class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components = 0

        adjList = {node:[] for node in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)
            for nei in adjList[node]:
                dfs(nei)

            return 1

        for i in range(n):
            components += dfs(i)

        return components
            
            