# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        dummy=ListNode()
        dummy.next=head
        prev=dummy

        while head and head.next:
            if head.val == head.next.val:
                prev.next=head.next
            else:
                prev=prev.next
            head=head.next
        return dummy.next
            

        