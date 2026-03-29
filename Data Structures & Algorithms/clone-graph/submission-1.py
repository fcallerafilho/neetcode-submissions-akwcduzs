"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node, adjList):
            if node in adjList:
                return adjList[node]
            
            newNode = Node(node.val)
            adjList[node] = newNode
            for n in node.neighbors:
                newNode.neighbors.append(dfs(n, adjList))

            return newNode
        
        return dfs(node, {}) if node else None








