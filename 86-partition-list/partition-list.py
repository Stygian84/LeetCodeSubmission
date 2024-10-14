# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = ListNode(0)
        last = ListNode(0)
        dummy = first
        dummy2 = last

        while head:
            if head.val<x:
                first.next=ListNode(head.val)
                first = first.next
            else:
                last.next = ListNode(head.val)
                last = last.next
            head=head.next
        first.next = dummy2.next
        return dummy.next