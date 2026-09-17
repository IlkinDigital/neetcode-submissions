# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        curr1 = list1
        curr2 = list2
        res = None
        if list1.val < list2.val:
            res = curr1
            curr1 = curr1.next
        else:
            res = curr2
            curr2 = curr2.next

        head = res

        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                res.next = curr1
                curr1 = curr1.next
            else:
                res.next = curr2
                curr2 = curr2.next
            
            res = res.next

        if curr1 is None:
            res.next = curr2
        else:
            res.next = curr1

        return head


