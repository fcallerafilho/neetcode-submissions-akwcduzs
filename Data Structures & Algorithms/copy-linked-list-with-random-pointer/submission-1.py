"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return Node(0).next
            
        nodes = {} # old, new
        
        curr = head

        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next
        
        for old, new in nodes.items():
            tail = new
            tail.next = nodes[old.next] if nodes.get(old.next, 0) != 0 else None
            tail.random = nodes[old.random] if nodes.get(old.random, 0) != 0 else None
            tail = tail.next

        return nodes[head]

        
            