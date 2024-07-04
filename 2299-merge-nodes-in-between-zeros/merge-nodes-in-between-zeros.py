# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        slow=head.next

        total=0
        while slow.next:
            if slow.val==0:
                head=head.next
                head.next=ListNode(total)
                total=0
            else:
                total+=slow.val
            print(total)
            slow=slow.next

        head=head.next
        head.next=ListNode(total)
        return dummy.next.next

            