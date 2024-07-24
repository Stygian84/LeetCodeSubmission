# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ls=[str(head.val)]
        while head and head.next:
            head=head.next
            ls.append(str(head.val))
            
        return int("".join(ls),2)
