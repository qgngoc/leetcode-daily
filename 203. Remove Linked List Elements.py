# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        while head:
            if head.val == val:
                head = head.next
                continue
            break
        
        init_head = head
        # print(init_head)
        while head:
            if head.next:
                if head.next.val == val:
                    head.next = head.next.next
                    continue
                head = head.next
                continue
            head = head.next

        return init_head