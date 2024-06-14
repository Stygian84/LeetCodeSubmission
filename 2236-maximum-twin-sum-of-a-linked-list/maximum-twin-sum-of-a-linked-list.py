# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        def reverseList(head): #from 206
            prev,curr=None,head
            while curr:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev

        slow=head 
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second_half=slow.next
        slow.next=None
        second_half=reverseList(second_half)

        max_sum=head.val+second_half.val
        while head and second_half:
            max_sum=max(max_sum,head.val+second_half.val)
            head=head.next
            second_half=second_half.next
        return max_sum
        