class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {node:[] for node in range(1, len(edges) + 1)}

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            visited = set()

            if not dfs(u, -1):
                return [u, v]
            
        return []