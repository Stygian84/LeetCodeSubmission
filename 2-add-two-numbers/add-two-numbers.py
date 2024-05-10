# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        values = []
        current = l1
        current2 = l2
        carry=False
        stop=False
        gcarry=False
        # This while is to sum 2 listnode if l1.length>l2.length
        while current:
            try:
                if carry:
                    if stop:
                        sum1 = current.val+1
                    else:
                        sum1 = current.val+current2.val+1
                else:
                    if stop:
                        sum1 = current.val
                    else:
                        sum1 = current.val+current2.val
            except:
                try:
                    values.append(current.val)
                except:
                    continue
            
            carry=False
            if sum1>=10:
                carry=True
                sum1-=10
            gcarry=carry

            values.append(sum1)
            try:
                current = current.next
            except:
                continue
            try:
                current2 = current2.next
                if current2==None:
                    stop=True
            except:
                stop=True
                continue
        
        # This while is to sum l1 and l2 if l2.length > l1.length
        try:
            while current2:
                if carry:
                    sum1 = current2.val+1
                else:
                    sum1 = current2.val
                carry=False
                if sum1>=10:
                    carry=True
                    sum1-=10
                gcarry=carry

                values.append(sum1)
                try:
                    current2 = current2.next
                    if current2==None:
                        stop=True
                except:
                    stop=True
                    continue
        except:
            pass
        
        # This is to add 1 or 0 if got extra carry
        if gcarry:
            value_exception = values[-1]+1
            if value_exception >10:
                values.append(value_exception-10)
                values.append(1)
            else:
                values.append(1)
        
        # convert answer to ListNode
        head = ListNode(values[0])
        current = head
        for item in values[1:]:
            current.next = ListNode(item)
            current = current.next
        
        return head
        

        
        