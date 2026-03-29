# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        
        for i in range(1, len(lists)):
            merged = self.mergeTwoLists(lists[i], lists[i-1])
            lists[i] = merged

        return lists[-1]


    def mergeTwoLists(self, l1: List[Optional[ListNode]], l2: List[Optional[ListNode]]) -> List[Optional[ListNode]]:
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next

        tail.next = l1 or l2
        
        return dummy.next