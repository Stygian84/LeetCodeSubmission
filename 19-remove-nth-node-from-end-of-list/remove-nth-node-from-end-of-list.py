# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ls=[head]
        res=head
        while head and head.next:
            head=head.next
            ls.append(head)


        if len(ls)==n:
            if len(ls)>1:
                return ls[1]
            else:
                return None
        if ls[-n-1].next:
            if ls[-n].next:
                ls[-n-1].next = ls[-n].next
            else:
                ls[-n-1].next=None
        return res