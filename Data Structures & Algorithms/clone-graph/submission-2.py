"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = collections.deque()
        visit = set()

        q.append(node)
        visit.add(node)

        oldToNew = {}
        oldToNew[node] = Node(val = node.val)
        
        while len(q) > 0:
            for i in range(len(q)):
                curr = q.popleft()
                
                for nei in curr.neighbors:
                    if nei not in oldToNew:
                        oldToNew[nei] = Node(val = nei.val)
                    oldToNew[curr].neighbors.append(oldToNew[nei])

                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)
                    
        return oldToNew[node]