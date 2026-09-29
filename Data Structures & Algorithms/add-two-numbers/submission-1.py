# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        buffer = 0
        while l1 is not None or l2 is not None or buffer > 0:
            value = 0

            if l1 is not None:
                value += l1.val
                l1 = l1.next
            if l2 is not None:
                value += l2.val
                l2 = l2.next
            if buffer > 0:
                value += buffer
                buffer = 0
            
            if value > 9:
                buffer += value // 10
                value %= 10

            curr.next = ListNode(value, None)
            curr = curr.next
        
        return head.next





