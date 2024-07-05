# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ls=[]
        if not head or not head.next:
            return [-1,-1]
        
        i=0
        prev=head.val #1
        head=head.next
        current=head.val #2

        min_distance=math.inf
        while head.next:

            head=head.next
            nex=head.val #3

            if (current<prev and current<nex) or (current>prev and current>nex):
                if len(ls)>0:
                    difference = i-ls[-1]
                    if difference<min_distance:
                        min_distance = difference
                ls.append(i)


            prev=current #1->2
            current=nex #2->3
            i+=1
        
        if len(ls)<2:
            return [-1,-1]
        
        #find min and max dist
        max_distance = ls[-1]-ls[0]

        return [min_distance,max_distance]

