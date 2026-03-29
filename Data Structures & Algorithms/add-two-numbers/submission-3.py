# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = ListNode(0)

        while l1 and l2:
            if not l1.next:
                    l1.next = ListNode(0)
            elif not l2.next:
                    l2.next = ListNode(0)
            if l1.val + l2.val + carry.val < 10:
                tail.next = ListNode(l1.val + l2.val + carry.val)
                carry.next = ListNode(0)
            else:
                val = l1.val + l2.val + carry.val
                tail.next = ListNode(val % 10)
                carry.next = ListNode((val // 10) if val > 10 else 1)

            print(l1.val, l2.val)
            l1 = l1.next
            l2 = l2.next
            tail = tail.next
            carry = carry.next
                
        if carry and carry.val != 0:
            tail.next = carry

        return dummy.next            
        