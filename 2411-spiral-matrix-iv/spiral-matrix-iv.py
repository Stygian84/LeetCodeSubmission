# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res=[[0]*n for i in range(m)]
        top,bottom=0,m-1
        left,right=0,n-1
        direction=0
        
        num = -1
        if head :
            num = head.val

        while top<=bottom and left<=right:
            
            if direction==0:
                for i in range(left,right+1):
                    if head :
                        num = head.val
                        head=head.next
                    else :
                        num = -1
                    res[top][i] = num
                top+=1
                
            elif direction==1:
                for i in range(top,bottom+1):
                    if head :
                        num = head.val
                        head=head.next
                    else :
                        num = -1
                    res[i][right] = num
                right-=1

            elif direction==2:
                for i in range(right,left-1,-1):
                    if head :
                        num = head.val
                        head=head.next
                    else :
                        num = -1
                    res[bottom][i] = num
                bottom-=1

            elif direction==3:
                for i in range(bottom,top-1,-1):
                    if head :
                        num = head.val
                        head=head.next
                    else :
                        num = -1
                    res[i][left] = num
                left+=1

            direction=(direction+1)%4
        
        return res
        