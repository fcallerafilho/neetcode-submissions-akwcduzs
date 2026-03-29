# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        node = head
        seen.add(node)

        while node:
            node = node.next
            if node in seen:
                return True
            seen.add(node)
            
        return False