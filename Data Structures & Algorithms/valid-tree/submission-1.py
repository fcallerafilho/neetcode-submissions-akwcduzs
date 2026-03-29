class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {node:[] for node in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        print(adjList)
        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        if not dfs(0, -1):
            return False
        
        for i in range(n):
            if i in visit:
                continue
            else:
                return False

        return True



            