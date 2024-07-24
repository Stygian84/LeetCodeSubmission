# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            a = head
            b = head.next
            
            prev.next = b
            a.next = b.next
            b.next = a
            
            prev = a
            head = a.next
        
        return dummy.next