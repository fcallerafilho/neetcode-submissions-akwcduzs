# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        elif not head.next:
            return False
        
        left = head
        right = left.next

        while right.next:
            if left.val >= right.val:
                return True
            right = right.next
            left = left.next

        return False





            




            