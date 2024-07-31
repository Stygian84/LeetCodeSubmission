# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if k==0:
            return head

        n=1
        dummy = head
        while dummy.next:
            dummy=dummy.next
            n+=1
        k=k%n
        if k==0:
            return head

        dummy.next = head
        steps = n-k
        new_end = head

        for _ in range(steps-1):
            new_end = new_end.next
        
        new_head = new_end.next
        new_end.next = None
        return new_head