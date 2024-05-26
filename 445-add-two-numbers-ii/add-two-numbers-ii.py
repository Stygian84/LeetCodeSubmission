# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=[]
        s2=[]
        def addToStack(stack,list):
            while list:
                stack.append(list.val)
                list=list.next
            return stack
        
        addToStack(s1, l1)
        addToStack(s2, l2)
        carry = 0
        result_head = None
        
        while s1 or s2 or carry:
            sum_val = carry
            if s1:
                sum_val += s1.pop()
            if s2:
                sum_val += s2.pop()
            
            carry=sum_val// 10
            digit=sum_val%10
            
            new_node = ListNode(digit)
            new_node.next = result_head
            result_head = new_node
        return result_head