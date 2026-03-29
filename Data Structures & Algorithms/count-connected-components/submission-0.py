class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components = 0

        adjList = {node:[] for node in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        def dfs(node, parent):
            if node in visited:
                return 0

            visited.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue
                dfs(nei, node)

            return 1

        for i in range(n):
            if i in visited:
                continue
            components += dfs(i, -1)

        return components
            
            