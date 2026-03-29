# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        
        curr = head

        while curr:
            l += 1
            curr = curr.next

        if l == 1:
            return None

        index = l - n 

        if index == 0:
            return head.next

        curr2 = head
        prev = None

        while index > 0:
            prev = curr2
            curr2 = curr2.next
            index -= 1

        prev.next = prev.next.next

        return head


