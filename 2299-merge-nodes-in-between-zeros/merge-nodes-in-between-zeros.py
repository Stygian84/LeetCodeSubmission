# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        res = dummy
        current = head.next

        total = 0
        while current:
            if current.val == 0 :
                res.next = ListNode(total)
                res = res.next
                total=0
            else:
                total += current.val
            
            current=current.next
        return dummy.next
            