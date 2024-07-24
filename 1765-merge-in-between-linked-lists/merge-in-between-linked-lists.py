# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        count=0
        res = list1
        A = list1
        B = list1
        while B and B.next:
            if count<a-1:
                A=A.next
            if count<b:
                B=B.next
            else:
                break
            count+=1
        
        A.next=list2
        while list2 and list2.next:
            list2=list2.next
        list2.next=B.next


        return res