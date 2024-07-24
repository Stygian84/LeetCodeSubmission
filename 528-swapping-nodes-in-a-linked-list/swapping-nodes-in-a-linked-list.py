# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = head

        k-=1
        ls=[]
        while head and head.next:
            ls.append(head)
            head=head.next
        ls.append(head)

        if len(ls)<=1:
            return res
        ls[k].val,ls[-k-1].val=ls[-k-1].val,ls[k].val
        return res