# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt_node = head
        list_size = 0

        while cnt_node:
            cnt_node = cnt_node.next
            list_size += 1
        
        groups_left = list_size // k
        curr_size = 0

        curr = head
        prev = None

        first_group = True

        prev_group_tail = head
        group_head = None
        
        while groups_left:
            if curr_size % k == 0:
                group_head = curr

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            curr_size += 1

            if curr_size % k == 0:
                if first_group:
                    head = prev
                    first_group = False
                else:
                    prev_group_tail.next = prev
                    prev_group_tail = group_head

                prev = None
                groups_left -= 1

        if group_head:
            group_head.next = curr

        return head
