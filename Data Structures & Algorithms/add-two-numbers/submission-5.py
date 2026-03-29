# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        
            if val < 10:
                tail.next = ListNode(val)
                carry = 0
            else:
                tail.next = ListNode(val % 10)
                carry = 1

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            tail = tail.next
                

        return dummy.next   