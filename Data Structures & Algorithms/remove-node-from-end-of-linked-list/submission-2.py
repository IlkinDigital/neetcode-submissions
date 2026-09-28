# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0

        curr = head
        while curr is not None:
            sz += 1
            curr = curr.next
        
        ith = sz - n
        
        if ith == 0:
            return head.next

        curr = head
        prev = None
        for _ in range(ith):
            prev = curr
            curr = curr.next

        prev.next = curr.next

        return head


