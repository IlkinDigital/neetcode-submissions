# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        record = set()

        while head is not None:
            record.add(head)

            if head.next in record:
                return True
            head = head.next
        
        return False
        