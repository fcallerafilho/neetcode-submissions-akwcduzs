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

        curr = head
        prev = None
        first_group = True

        group_head = None
        prev_group_tail = None
        
        processed_count = 0

        while list_size >= k:
            if processed_count % k == 0:
                group_head = curr

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            processed_count += 1

            if processed_count % k == 0:
                if first_group:
                    head = prev
                    first_group = False
                else:
                    prev_group_tail.next = prev

                prev_group_tail = group_head
                group_head.next = curr
                prev = None
                list_size -= k

        return head
