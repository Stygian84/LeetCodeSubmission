# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        result=head

        while head and head.next:
            res = math.gcd(head.val,head.next.val)
            dummy=ListNode(res)
            dummy.next=head.next
            head.next=dummy

            head=head.next.next

        return result